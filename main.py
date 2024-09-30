import requests
import random

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    url = "https://api.themoviedb.org/3/trending/person/day?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiYTcxZTk2OTlhNDBlMjExMDE3ZTQ1YzI1OGQ1NDk5MyIsIm5iZiI6MTcyNzczMzU2NS45OTYzNDksInN1YiI6IjY2ZmIxZTgwM2EwZjVhMDhjOGYxYWQ0ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.0mmnhNxn7GH8xFho5zDJYAXr83Iaj9t2MkdheyWrIXI"
    }

    response = requests.get(url, headers=headers)

    json_response = response.json()
    results_count = len(json_response['results'])
    random_index = random.randint(0, results_count)
    random_person = json_response['results'][random_index]

    minor_rating = 9999999
    worst_movie = ''
    for movie in random_person['known_for']:
        if movie['popularity'] < minor_rating:
            worst_movie = movie

    return f"La pelicula menos popular de {random_person['name']} es {worst_movie['title']} y trabajo en el departamento de {random_person['known_for_department']}"
