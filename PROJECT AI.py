import requests
from datetime import datetime
import pytz
import folium
from folium.plugins import MarkerCluster
import webbrowser

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Constants
OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_SEARCH_URL = os.getenv("GEMINI_SEARCH_URL")


# Function to fetch weather data from OpenWeatherMap
def fetch_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None


# Function to preprocess weather data
def preprocess_weather_data(data):
    # Extract relevant features
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    weather_description = data["weather"][0]["description"]
    pressure = data["main"]["pressure"]

    # Convert temperature from Kelvin to Celsius
    temperature_celsius = temperature - 273.15

    return temperature_celsius, humidity, wind_speed, weather_description, pressure


# Function to train predictive model
def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return model, accuracy


# Function to predict weather hazard using trained model
def predict_weather_hazard(model, X):
    return model.predict(X)


# Function to generate remarks by Gemini AI
def generate_remarks(weather_description, humidity, pressure):
    remarks = ""
    if "rain" in weather_description.lower():
        remarks += "Expect rainfall. "
    elif "clear" in weather_description.lower():
        remarks += "Clear skies expected. "
    else:
        remarks += "Weather condition uncertain. "

    if humidity > 80:
        remarks += "High humidity levels detected. "
    elif humidity < 30:
        remarks += "Low humidity levels detected. "

    if pressure < 1000:
        remarks += "Low atmospheric pressure detected. "
    elif pressure > 1020:
        remarks += "High atmospheric pressure detected. "

    return remarks.strip()


# Function to interact with Gemini AI for natural disaster information
def interact_with_gemini_ai(query):
    try:
        url = GEMINI_SEARCH_URL + query
        response = requests.get(url)
        response.raise_for_status()
        return response.json()["response"]
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return "Failed to get information from Gemini AI."


# Function to generate HTML content for the chatbot panel
def generate_chatbot_panel_content():
    chatbot_panel_content = """
    <div id="chatbot-panel" style="position: fixed; right: 20px; bottom: 20px; width: 300px; height: 400px; background-color: #f0f0f0; border: 1px solid #ccc; border-radius: 5px; overflow: hidden;">
        <div id="chat-container" style="padding: 10px; max-height: 300px; overflow-y: auto;">
            <div id="chat-messages"></div>
            <input type="text" id="user-input" placeholder="Type your message..." style="width: calc(100% - 22px); margin-top: 10px; padding: 5px; border: 1px solid #ccc;">
        </div>
    </div>
    <script>
    var chatMessages = document.getElementById('chat-messages');
    var userInput = document.getElementById('user-input');

    // Function to add message to the chatbox
    function addMessage(sender, message) {
        var messageElement = document.createElement('div');
        messageElement.innerHTML = '<strong>' + sender + ':</strong> ' + message;
        chatMessages.appendChild(messageElement);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    // Function to handle user input
    function handleUserInput() {
        var userInputText = userInput.value.trim();
        if (userInputText !== '') {
            addMessage('You', userInputText);
            console.log('User Input:', userInputText); // Log user input
            // Send user input to Gemini AI and display response
            // Replace the API_KEY with your Gemini AI API key and modify the URL if necessary
            fetch('https://www.gemini.com/api?query=' + encodeURIComponent(userInputText))
            .then(response => response.json())
            .then(data => {
                var geminiResponse = data.response;
                console.log('Gemini AI Response:', geminiResponse); // Log Gemini AI response
                addMessage('Gemini AI', geminiResponse);
            })
            .catch(error => console.error('Error:', error));
            userInput.value = '';
        }
    }

    // Event listener for user input
    userInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            handleUserInput();
        }
    });
</script>
    """
    return chatbot_panel_content


# Main function
def main():
    # Take user input for the city
    # city = input("Enter the city: ")
    # fetch the current location using ipinfo site
    response = requests.get("https://ipinfo.io")
    city = response.json()["city"]

    # Fetch weather data for the entered city
    weather_data = fetch_weather_data(city)
    if not weather_data:
        print("Failed to fetch weather data.")
        return

    # Preprocess weather data
    temperature, humidity, wind_speed, weather_description, pressure = preprocess_weather_data(weather_data)

    # Example model training (replace with actual training)
    X = [[25, 70, 5, 1000], [20, 80, 3, 990]]  # Example features
    y = [0, 1]  # Example labels (0: No hazard, 1: Hazard)
    model, accuracy = train_model(X, y)

    # Predict weather hazard
    hazard_prediction = predict_weather_hazard(model, [[temperature, humidity, wind_speed, pressure]])[0]

    # Generate remarks by Gemini AI
    remarks = generate_remarks(weather_description, humidity, pressure)

    # Generate HTML content for the chatbot panel
    chatbot_panel_content = generate_chatbot_panel_content()

    # Create a map
    map = folium.Map(location=[weather_data["coord"]["lat"], weather_data["coord"]["lon"]], zoom_start=10)

    # Add wind layer
    wind_url = "https://tile.openweathermap.org/map/wind_new/{z}/{x}/{y}.png?appid=8ee63116fa89d1502e75d1f92a7eee14"
    folium.TileLayer(wind_url, attr="OpenWeatherMap Wind").add_to(map)

    # Add rainfall layer
    rainfall_url = "https://tile.openweathermap.org/map/precipitation_new/{z}/{x}/{y}.png?appid=8ee63116fa89d1502e75d1f92a7eee14"
    folium.TileLayer(rainfall_url, attr="OpenWeatherMap Rainfall").add_to(map)

    # Add humidity layer
    humidity_url = "https://tile.openweathermap.org/map/humidity_new/{z}/{x}/{y}.png?appid=8ee63116fa89d1502e75d1f92a7eee14"
    folium.TileLayer(humidity_url, attr="OpenWeatherMap Humidity").add_to(map)

    # Add pressure contour layer
    pressure_url = "https://tile.openweathermap.org/map/pressure_new/{z}/{x}/{y}.png?appid=8ee63116fa89d1502e75d1f92a7eee14"
    folium.TileLayer(pressure_url, attr="OpenWeatherMap Pressure").add_to(map)

    # Add marker to the map with weather information and remarks
    popup_html = f"<b>{city} Weather</b><br>" \
                 f"<b>Description:</b> {weather_description}<br>" \
                 f"<b>Temperature:</b> {temperature}°C<br>" \
                 f"<b>Humidity:</b> {humidity}%<br>" \
                 f"<b>Wind Speed:</b> {wind_speed} m/s<br>" \
                 f"<b>Atmospheric Pressure:</b> {pressure} hPa<br>" \
                 f"<b>Remarks:</b> {remarks}"
    folium.Marker([weather_data["coord"]["lat"], weather_data["coord"]["lon"]],
                  popup=folium.Popup(popup_html, max_width=300)).add_to(map)

    # Save the map to an HTML file
    map.save("weather_map.html")

    # Generate and save chatbot panel HTML to a separate file
    with open("chatbot_panel.html", "w") as chatbot_panel_file:
        chatbot_panel_file.write(chatbot_panel_content)

    # Open the map HTML file in the default web browser
    webbrowser.open("weather_map.html")

    # Print alerts if hazard predicted
    if hazard_prediction == 1:
        tz = pytz.timezone('Africa/Nairobi')
        current_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        print(f"Hazard predicted in {city} at {current_time}. Take necessary precautions.")
    else:
        print(f"No hazard predicted in {city}.")


if __name__ == "__main__":
    main()
