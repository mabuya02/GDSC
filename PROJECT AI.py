
import requests
from datetime import datetime
import pytz
import folium
from folium.plugins import MarkerCluster
import webbrowser
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


# Function to generate HTML content for the search bar
def generate_search_bar_content():
    search_bar_content = """
    <div id="search-bar" style="position: fixed; top: 20px; left: 20px;">
        <input type="text" id="city-input" placeholder="Enter city name">
        <button onclick="fetchWeatherData()">Search</button>
    </div>
    <script>
    // Function to fetch weather data for the entered city
    function fetchWeatherData() {
        var city = document.getElementById('city-input').value.trim();
        if (city !== '') {
            fetch('/weather?city=' + encodeURIComponent(city))
            .then(response => response.json())
            .then(data => {
                // Process weather data and update map
                // Example: Update map with new marker for the city
                console.log('Weather Data:', data);
            })
            .catch(error => console.error('Error:', error));
        }
    }
    </script>
    """
    return search_bar_content


# Function to create folium map
def create_map(location):
    map = folium.Map(location=location, zoom_start=10)
    return map


# Main function
def main():
    # Generate HTML content for the chatbot panel and search bar
    chatbot_panel_content = generate_chatbot_panel_content()
    search_bar_content = generate_search_bar_content()

    # Generate and save chatbot panel HTML to a separate file
    with open("chatbot_panel.html", "w") as chatbot_panel_file:
        chatbot_panel_file.write(chatbot_panel_content)

    # Generate and save search bar HTML to a separate file
    with open("search_bar.html", "w") as search_bar_file:
        search_bar_file.write(search_bar_content)

    # Open the map HTML file in the default web browser
    webbrowser.open("chatbot_panel.html")
    webbrowser.open("search_bar.html")


if __name__ == "__main__":
    main()
