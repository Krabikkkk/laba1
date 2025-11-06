from exceptions import InvalidGenreError


def check_genre_name(name):
    if name is None:
        raise InvalidGenreError("Название жанра не может быть None")
    if not isinstance(name, str):
        raise InvalidGenreError("Название жанра должно быть строкой")
    if name.strip() == "":
        raise InvalidGenreError("Название жанра не может быть пустым")
    return name.strip()


def check_genre_description(description):
    if description is None:
        return None
    if not isinstance(description, str):
        raise InvalidGenreError("Описание жанра должно быть строкой или отсутствовать")
    if description.strip() == "":
        raise InvalidGenreError("Описание жанра не может быть пустой строкой")
    return description.strip()


def check_genre_id(genre_id):
    if genre_id is None:
        raise InvalidGenreError("ID жанра не указан")
    try:
        genre_id = int(genre_id)
    except (ValueError, TypeError):
        raise InvalidGenreError("ID жанра должен быть целым числом")
    if genre_id <= 0:
        raise InvalidGenreError(f"ID жанра должен быть положительным. Получено: {genre_id}")
    return genre_id


class Genre:
    def __init__(self, name: str, description: str | None, ID: int):
        self.name = check_genre_name(name)
        self.description = check_genre_description(description)
        self.ID = check_genre_id(ID)

    def __str__(self):
        if self.description:
            return f"Жанр - {self.name}, описание: {self.description}, ID - {self.ID}"
        else:
            return f"Жанр - {self.name}, ID - {self.ID}"