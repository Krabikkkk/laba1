from exceptions import InvalidCollectionError

class Collection:
    @staticmethod
    def check_collection_id(collection_id):
        if collection_id is None:
            raise InvalidCollectionError("ID подборки не указан")
        try:
            collection_id = int(collection_id)
        except (ValueError, TypeError):
            raise InvalidCollectionError("ID подборки должен быть целым числом")
        if collection_id <= 0:
            raise InvalidCollectionError(f"ID подборки должен быть положительным. Получено: {collection_id}")
        return collection_id

    @staticmethod
    def check_collection_name(name):
        if name is None:
            raise InvalidCollectionError("Название подборки не указано")
        if not isinstance(name, str):
            raise InvalidCollectionError("Название подборки должно быть строкой")
        if name.strip() == "":
            raise InvalidCollectionError("Название подборки не может быть пустым")
        return name.strip()

    @staticmethod
    def check_collection_movie_ids(movie_ids):
        if movie_ids is None:
            raise InvalidCollectionError("Список фильмов не указан")
        if not isinstance(movie_ids, list):
            raise InvalidCollectionError("Список фильмов должен быть типом list")
        valid_ids = []
        for i, mid in enumerate(movie_ids):
            try:
                mid = int(mid)
            except (ValueError, TypeError):
                raise InvalidCollectionError(f"ID фильма на позиции {i + 1} должен быть целым числом")
            if mid <= 0:
                raise InvalidCollectionError(f"ID фильма на позиции {i + 1} должен быть положительным. Получено: {mid}")
            valid_ids.append(mid)
        return valid_ids

    def __init__(self, ID: int, name: str, movie_ids: list[int]):
        self.ID = self.check_collection_id(ID)
        self.name = self.check_collection_name(name)
        self.movie_ids = self.check_collection_movie_ids(movie_ids)

    def __str__(self):
        return f"Подборка '{self.name}' (ID={self.ID}): {len(self.movie_ids)} фильмов"