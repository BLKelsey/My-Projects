import requests

# Get user input
city_name = input("Enter city name: ").strip()
state_code = input("Enter state code (press Enter if none): ").strip()
country_code = input("Enter country code (e.g., US, LB, FR): ").strip()

# Get your API key from api site
api_key = "4391550fbe090859f16e877942ba2271"

# Build the location string correctly - test
if state_code and country_code:
    location = f"{city_name},{state_code},{country_code}"
elif country_code:
    location = f"{city_name},{country_code}"
else:
    location = city_name

# Build API URL
api_url = (
    "https://api.openweathermap.org/data/2.5/weather"
    + "?q=" + location
    + "&units=imperial"
    + "&appid=" + api_key
)

# Make request
response = requests.get(api_url)
data = response.json()

# Handle response
if response.status_code != 200:
    print("Error:", data.get("message", "Something went wrong"))
else:
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°F")
    print("Weather:", data["weather"][0]["description"])
