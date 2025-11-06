import json
from user import User
from movie import Movie
from genre import Genre


def delete_user_by_id(users: list[User], user_id: int) -> bool:
    for i, user in enumerate(users):
        if user.ID == user_id:
            users.pop(i)
            print(f"Пользователь с ID {user_id} удалён")
            return True
    print(f"Пользователь с ID {user_id} не найден")
    return False
def load_data_from_json(filename: str):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Файл {filename} не найден. Создаём пустые данные.")
        return [], [], []
    except json.JSONDecodeError:
        print(f"Файл {filename} повреждён.")
        return [], [], []

    users = []
    for i, user_data in enumerate(data.get("users", []), 1):
        try:
            user = User(
                username=user_data["username"],
                age=user_data["age"],
                ID=user_data["ID"]
            )
            users.append(user)
        except Exception as e:
            print(f"Ошибка при создании пользователя {i}: {e}")

    movies = []
    for i, movie_data in enumerate(data.get("movies", []), 1):
        try:
            movie = Movie(
                title=movie_data["title"],
                genre=movie_data["genre"],
                duration=movie_data["duration"],
                ID=movie_data["ID"]
            )
            movies.append(movie)
        except Exception as e:
            print(f"Ошибка при создании фильма {i}: {e}")

    genres = []
    for i, genre_data in enumerate(data.get("genres", []), 1):
        try:
            genre = Genre(
                name=genre_data["name"],
                description=genre_data.get("description"),  # может отсутствовать
                ID=genre_data["ID"]
            )
            genres.append(genre)
        except Exception as e:
            print(f"Ошибка при создании жанра {i}: {e}")

    return users, movies, genres
