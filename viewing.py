from exceptions import InvalidViewingError


class Viewing:

    def check_viewing_user_id(user_id):
        if user_id is None:
            raise InvalidViewingError("ID пользователя не указан")
        try:
            user_id = int(user_id)
        except (ValueError, TypeError):
            raise InvalidViewingError("ID пользователя должен быть целым числом")
        if user_id <= 0:
            raise InvalidViewingError(f"ID пользователя должен быть положительным. Получено: {user_id}")
        return user_id

    def check_viewing_movie_id(movie_id):
        if movie_id is None:
            raise InvalidViewingError("ID фильма не указан")
        try:
            movie_id = int(movie_id)
        except (ValueError, TypeError):
            raise InvalidViewingError("ID фильма должен быть целым числом")
        if movie_id <= 0:
            raise InvalidViewingError(f"ID фильма должен быть положительным. Получено: {movie_id}")
        return movie_id

    def check_viewing_watch_time(watch_time):
        if watch_time is None:
            raise InvalidViewingError("Время просмотра не указано")
        if not isinstance(watch_time, str):
            raise InvalidViewingError(
                "Время просмотра должно быть строкой (например, '01:23:45' или '2025-04-05T20:30')")
        if watch_time.strip() == "":
            raise InvalidViewingError("Время просмотра не может быть пустым")
        return watch_time.strip()

    def __init__(self, user_id: int, movie_id: int, watch_time: str):
        self.user_id = self.check_viewing_user_id(user_id)
        self.movie_id = self.check_viewing_movie_id(movie_id)
        self.watch_time = self.check_viewing_watch_time(watch_time)

    def __str__(self):
        return f"Просмотр: пользователь {self.user_id} остановился на фильме {self.movie_id} во время '{self.watch_time}'"