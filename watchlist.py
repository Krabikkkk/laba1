from exceptions import InvalidWatchlistError


class Watchlist:

    def check_watchlist_user_id(user_id):
        if user_id is None:
            raise InvalidWatchlistError("ID пользователя не указан")
        try:
            user_id = int(user_id)
        except (ValueError, TypeError):
            raise InvalidWatchlistError("ID пользователя должен быть целым числом")
        if user_id <= 0:
            raise InvalidWatchlistError(f"ID пользователя должен быть положительным. Получено: {user_id}")
        return user_id

    def check_watchlist_movie_ids(movie_ids):
        if movie_ids is None:
            raise InvalidWatchlistError("Список фильмов не указан")
        if not isinstance(movie_ids, list):
            raise InvalidWatchlistError("Список фильмов должен быть типом list")
        if len(movie_ids) > 20:
            raise InvalidWatchlistError(f"Максимум 20 фильмов в списке. Передано: {len(movie_ids)}")
        valid_ids = []
        for i, mid in enumerate(movie_ids):
            try:
                mid = int(mid)
            except (ValueError, TypeError):
                raise InvalidWatchlistError(f"ID фильма на позиции {i + 1} должен быть целым числом")
            if mid <= 0:
                raise InvalidWatchlistError(f"ID фильма на позиции {i + 1} должен быть положительным. Получено: {mid}")
            valid_ids.append(mid)
        return valid_ids

    def check_watchlist_name(name):
        if name is None:
            raise InvalidWatchlistError("Название списка не указано")
        if not isinstance(name, str):
            raise InvalidWatchlistError("Название списка должно быть строкой")
        if name.strip() == "":
            raise InvalidWatchlistError("Название списка не может быть пустым")
        return name.strip()

    def __init__(self, user_id: int, movie_ids: list[int], name: str):
        self.user_id = self.check_watchlist_user_id(user_id)
        self.movie_ids = self.check_watchlist_movie_ids(movie_ids)
        self.name = self.check_watchlist_name(name)

    def __str__(self):
        return f"Список '{self.name}' пользователя {self.user_id}: {len(self.movie_ids)} фильмов"