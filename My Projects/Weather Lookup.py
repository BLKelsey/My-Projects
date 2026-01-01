import requests                                               # Imports the requests library for making HTTP requests

city_name = input("Enter city name: ")                        # Asks the user to enter a city name
state_code = input("Enter state code (e.g., OH, IL, MO): ")   # Asks the user for state

api_key = "4391550fbe090859f16e877942ba2271"                   # Stores the OpenWeatherMap API key (keep this private)

api_url = (                                                    # Build the full API request URL
    "https://api.openweathermap.org/data/2.5/weather"         # Base OpenWeatherMap weather endpoint
    + "?q=" + city_name + "," + state_code                    # City, state remove ambiguity
    + "&units=imperial"                                       # Request temperature in Fahrenheit
    + "&appid=" + api_key                                     # Attach your API key for authentication
)

response = requests.get(api_url)                                # Sends the GET request to the weather API
data = response.json()                                          # Converts the API response from JSON to a Python dictionary

# Check if request was successful
if response.status_code != 200:                                 # If the API did NOT return success
    print("Error:", data.get("message", "Something went wrong"))# Print the error message from the API
else:
    print("City:", data["name"])                               # Displays the city name from the response
    print("Temperature:", data["main"]["temp"], "°F")          # Displays the current temperature
    print("Weather:", data["weather"][0]["description"])       # Displays a short weather description
