import json

from movie import Movie
from user import User


with open("1.json", "r", encoding= "UTF-8") as file:
    data = json.load(file)
    movies_data = data.get("movies", [])
    movies = []
    for movie_value in movies_data:
        movie_obj = Movie(
            title=movie_value["title"],
            genre=movie_value["genre"],
            duration=movie_value["duration"]
        )
        movies.append(movie_obj)

