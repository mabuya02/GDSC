# Inspiration

Navigating through the landscape of disaster management software and getting started with contributions can indeed be challenging. We wanted to simplify this landscape for beginners and added a roadmap for those who want to delve deeper into the field of Disaster Management.This platform is developed in a way that it can guide newcomers and help them learn concepts such as real-time data monitoring, alert protocols, and USSD technology, even if they contribute to this project. 

This is because of the tools used in this project such as *real-time flood monitoring systems, **FEMA App, **SMART water Monitoring and Alert system⁴, and a **conceptual design of Smart Management System for Flooding Disaster*.



# ⚙ What it does -

The main aim of this project is to develop a disaster management software that will send flood alerts to users via USSD, making it accessible to everyone. This initiative is inspired by the recent flood cases in Kenya and aims to provide a timely warning to communities in vulnerable areas, enabling residents to prepare and take necessary precautions. The availability of real-time data ensures that warnings are accurate and tailored to specific locations, maximizing their effectiveness.


# 🔧 How we built it-

Here's a step-by-step explanation of how we built the disaster management software:
1. *User Location Data*: We first determine the current location of the user. This is crucial as it allows us to provide location-specific weather predictions and flood alerts.
2. *OpenWeather API*: We use the OpenWeather API to pull real-time weather data for the user's location. The OpenWeather API provides comprehensive weather data, including temperature, humidity, wind speed, and precipitation, which are all important factors in predicting floods.
3. *Data Processing*: The weather data pulled from the OpenWeather API is then processed and formatted in a way that can be used by the Gemini API. This might involve cleaning the data, handling missing values, and transforming the data into a suitable format.
4. *Gemini API*: We push the processed weather data to the Gemini API. Gemini is an AI technology that uses this data to predict the weather conditions and the likelihood of floods. It uses advanced machine learning algorithms to analyze the weather data and make accurate predictions.
5. *Flood Prediction*: Based on the analysis of the weather data, the Gemini API predicts if there are any floods expected in the user's location. It takes into account various factors such as the amount of rainfall, the rate of rainfall, the soil moisture content, and the topography of the area.
6. *Recommendations*: Based on the flood prediction, we generate recommendations for the users on what actions they should take. If a flood is expected, the software might recommend the users to evacuate the area, move to higher ground, or prepare their homes for the flood.
7. *USSD Alerts*: Finally, we send these recommendations to the users via USSD. USSD is a communication technology that is accessible on all types of mobile phones, making it a great choice for sending flood alerts to a wide range of users.

In summary, we use a combination of user location data, the OpenWeather API, data processing techniques, the Gemini API, flood prediction algorithms, recommendation generation, and USSD alerts to provide real-time flood alerts to users. This makes our disaster management software a comprehensive tool for managing and mitigating the impact of floods.



# 💪  Future Plans:
1. *Incorporate Sensor Data*: We plan to incorporate data from sensors that will be deployed in different places across countries. These sensors will collect real-time data, which will be relayed to our software. This data will be analyzed automatically using uniquely designed algorithms, and specific actions will be evoked via interpretation of the results by artificial intelligence.
2. *Python Project for Flood Relief Shelters*: We aim to develop a Python project that can be used by flood relief shelters. This software will be able to store and update details of affected victims, maintain an inventory of supplies, and find live geo stats of the flood-affected areas.
3. *Inventory Management*: The software will have a robust inventory management system. This will help in tracking supplies, reducing errors, saving time, and optimizing stock levels, enhancing the efficiency and effectiveness of disaster management.
4. *Live Geo Stats*: The software will provide live geo stats of flood-affected areas. This will help in real-time monitoring of the situation and aid in effective decision-making during disaster management.
5. *User Accessibility*: The software will be designed to be user-friendly and accessible to everyone. It will have a simple and intuitive interface that can be easily used by individuals with minimal technical knowledge.
6. *Continuous Improvement*: We plan to continuously improve and update the software based on user feedback and technological advancements. This will ensure that the software remains relevant and effective in managing disasters.
7. *Collaboration and Sharing*: The software will have features that allow for easy sharing of information and collaboration among different disaster management agencies. This will ensure a coordinated and effective response to disasters.
8. *Training and Support*: We will provide training and support to users to ensure they can effectively use the software. This will include user manuals, online tutorials, and customer support.These plans aim to make the software a comprehensive tool for disaster management, particularly for flood relief. It will not only help in immediate response to disasters but also in planning and preparedness, thereby reducing the impact of such events.




# :sunglasses: Accomplishments that we're proud of -
Although we were not familiar with deployemtn on Gemini and most of the tools and tech we used to build it, we tried and learned on the go to make it possible.

# 📚 What we learned -
We learnt about react and how to make use of all the tools according to the use case of our project even if they were different and sometimes caused a lot of trouble.