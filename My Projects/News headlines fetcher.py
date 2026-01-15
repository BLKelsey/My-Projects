import requests

api_key = "c986a8791de6476c86d374f1bd3bc78e"

news_sites = [
    "the-washington-times",
    "fox-news",
    "breitbart-news"
]


sources_string = ', '.join(news_sites)
# JOIN news_sites into a single string, separated by commas and STORING result in sources_string

request_url = "https://newsapi.org/v2/top-headlines?sources=" + sources_string + "&apiKey=" + api_key
# Builds the full URL for the API request by inserting your chosen sources and your API key

response = requests.get(request_url)
# Sends an HTTP GET request to NewsAPI using the URL above

data = response.json()
# Converts the API response from JSON text into a Python dictionary you can work with

if data["articles"]:                  # Checks if the "articles" list exists and is not empty
    for article in data["articles"]:  # Loops through each article returned by the API
        print(article["title"])       # Prints the headline/title of the article
        print(article["url"])         # Prints the link to the full article
        print()
else:
    print("No articles found")    # Runs if the "articles" list is empty or missing


