import json
from os import remove

from movie import Movie
from user import User
from cinema import Cinema

cinema = Cinema()
cinema.load_json_file("1.json")
cinema = cinema.delete_obj_of_cinema("movies", 0)
for movie in cinema.movies:
    print(movie.title)