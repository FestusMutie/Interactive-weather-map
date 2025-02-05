Weather Map App 🌍
An interactive weather map app built using Streamlit and Leafmap. The app allows users to view real-time temperature data for Nairobi or any other city. The map displays the temperature as a marker on the map, with the option to enter city names or latitude and longitude coordinates.

🛠 Features
Interactive Map: Displays real-time temperature data on a map.
City Search: Allows users to search for weather data by entering a city name (default is Nairobi).
Latitude/Longitude: Option to enter geographic coordinates manually.
Real-Time Data: Fetches temperature data via Open-Meteo API.
💡 How to Use
Run the App:
bash
Copy
Edit
streamlit run weather_map.py
Enter a City: Type a city name (e.g., Nairobi, Berlin) or use the default Nairobi.
Enter Coordinates: Alternatively, enter latitude and longitude to get the weather of a specific location.
View Temperature: The temperature of the location is shown on the map as a marker.
🌐 Live Example
The app will automatically display the weather for Nairobi when it starts. Users can search for any city or input coordinates to see its weather.

🛠 Installation Instructions
To run this app locally, follow these steps:

Clone the Repository (or download the project files):

bash
Copy
Edit
git clone https://github.com/yourusername/weather-map-app.git
Install Dependencies: Make sure you have Python installed (version 3.6 or higher). Then, install the required libraries using pip:

bash
Copy
Edit
pip install -r requirements.txt
Alternatively, you can install them manually:

bash
Copy
Edit
pip install streamlit leafmap requests geopy
Run the App:

bash
Copy
Edit
streamlit run weather_map.py
🖥️ Technologies Used
Streamlit: For building the web application.
Leafmap: To display the interactive weather map.
Open-Meteo API: Provides free weather data.
Geopy: For converting city names to geographic coordinates.# Interactive-weather-map
