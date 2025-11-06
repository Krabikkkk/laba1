from exceptions import InvalidWatchHistoryError


def check_watchhistory_user_id(user_id):
    if user_id is None:
        raise InvalidWatchHistoryError("ID пользователя не указан")
    try:
        user_id = int(user_id)
    except (ValueError, TypeError):
        raise InvalidWatchHistoryError("ID пользователя должен быть целым числом")
    if user_id <= 0:
        raise InvalidWatchHistoryError(f"ID пользователя должен быть положительным. Получено: {user_id}")
    return user_id


def check_watchhistory_movie_ids(movie_ids):
    if movie_ids is None:
        raise InvalidWatchHistoryError("Список фильмов не указан")
    if not isinstance(movie_ids, list):
        raise InvalidWatchHistoryError("Список фильмов должен быть типом list")
    if len(movie_ids) > 10:
        movie_ids = movie_ids[-10:]
    valid_ids = []
    for i, mid in enumerate(movie_ids):
        try:
            mid = int(mid)
        except (ValueError, TypeError):
            raise InvalidWatchHistoryError(f"ID фильма на позиции {i+1} должен быть целым числом")
        if mid <= 0:
            raise InvalidWatchHistoryError(f"ID фильма на позиции {i+1} должен быть положительным. Получено: {mid}")
        valid_ids.append(mid)
    return valid_ids


class WatchHistory:
    MAX_HISTORY = 10

    def __init__(self, user_id: int, movie_ids: list[int]):
        self.user_id = check_watchhistory_user_id(user_id)
        self.movie_ids = check_watchhistory_movie_ids(movie_ids)

    def add_movie(self, movie_id: int):
        if not isinstance(movie_id, int) or movie_id <= 0:
            raise InvalidWatchHistoryError("ID фильма должен быть положительным целым числом")
        self.movie_ids.append(movie_id)
        if len(self.movie_ids) > self.MAX_HISTORY:
            self.movie_ids.pop(0)  # Удаляем самый старый

    def __str__(self):
        return f"История пользователя {self.user_id}: последние {len(self.movie_ids)} фильмов"