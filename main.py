import json
from user import User
from movie import Movie
from genre import Genre


def load_to_json(file):
    try:
        with open(file, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print("файл не найден")
        return {"data": []}
    except json.JSONDecodeError:
        print("файл поврежден или не является валидным")
        return {"data": []}


users, movies, genres = [], [], []
data = load_to_json('data.json')
users = User.load_users_json(data["users"])
movies = Movie.load_movies_xml("data.xml")
genres = Genre.load_genres_xml("data.xml")











try:
    users.append(User("Bob", 12, 100))
except ValueError as error:
    print(error)
try:
    movies.append(Movie("Halk", "hz", 121, 110))
except ValueError as error:
    print(error)
User.delete_user(users, 3)

for  user in users:
    print(user)

for movie in movies:
    print(movie)


for genre in genres:
    print(genre)
