import requests

MOVIE_DB_URL = "https://api.themoviedb.org/3/search/movie?"
MOVIE_DB_API = "578f6159497928dc51b72571f0f08f4b"

parameters = {
    "api_key": MOVIE_DB_API,
    "query": "Harry Potter"
}

response = requests.get(MOVIE_DB_URL, params=parameters)
data = response.text
print(data)