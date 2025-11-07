from exceptions import InvalidMovieError

class Movie:

    @staticmethod
    def check_movie_title(title):
        if title is None:
            raise InvalidMovieError("Название фильма не может быть None")
        if not isinstance(title, str):
            raise InvalidMovieError("Название фильма должно быть строкой")
        if title.strip() == "":
            raise InvalidMovieError("Название фильма не может быть пустым")
        return title.strip()

    @staticmethod
    def check_movie_genre(genre):
        if genre is None:
            raise InvalidMovieError("Жанр фильма не может быть None")
        if not isinstance(genre, str):
            raise InvalidMovieError("Жанр фильма должен быть строкой")
        if genre.strip() == "":
            raise InvalidMovieError("Жанр фильма не может быть пустым")
        return genre.strip()

    @staticmethod
    def check_movie_duration(duration):
        if duration is None:
            raise InvalidMovieError("Длительность фильма не указана")
        try:
            duration = int(duration)
        except (ValueError, TypeError):
            raise InvalidMovieError("Длительность фильма должна быть целым числом (в минутах)")
        if duration <= 0:
            raise InvalidMovieError(f"Длительность фильма должна быть положительной. Получено: {duration} мин")
        return duration

    @staticmethod
    def check_movie_id(movie_id):
        if movie_id is None:
            raise InvalidMovieError("ID фильма не указан")
        try:
            movie_id = int(movie_id)
        except (ValueError, TypeError):
            raise InvalidMovieError("ID фильма должен быть целым числом")
        if movie_id <= 0:
            raise InvalidMovieError(f"ID фильма должен быть положительным. Получено: {movie_id}")
        return movie_id

    def __init__(self, title: str, genre: str, duration: int, ID: int):
        self.title = self.check_movie_title(title)
        self.genre = self.check_movie_genre(genre)
        self.duration = self.check_movie_duration(duration)
        self.ID = self. check_movie_id(ID)

    def __str__(self):
        return f"{self.title} ({self.genre}, {self.duration} мин), ID - {self.ID}"