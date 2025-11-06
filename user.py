from exceptions import InvalidUserError


def check_username(username):
    if username is None:
        raise InvalidUserError("Имя пользователя не может быть None")
    if not isinstance(username, str):
        raise InvalidUserError("Имя пользователя должно быть строкой")
    if username.strip() == "":
        raise InvalidUserError("Имя пользователя не может быть пустым")
    return username.strip()


def check_age(age):
    if age is None:
        raise InvalidUserError("Поле 'age' не может быть пустым")
    try:
        age = int(age)
    except (ValueError, TypeError):
        raise InvalidUserError("Возраст должен быть целым числом")
    if not (6 <= age <= 100):
        raise InvalidUserError(f"Возраст должен быть от 6 до 100 лет. Получено: {age}")
    return age


def check_ID(ID):
    if ID is None:
        raise InvalidUserError("Поле 'ID' не может быть пустым")
    try:
        ID = int(ID)
    except (ValueError, TypeError):
        raise InvalidUserError("ID должен быть целым числом")
    if ID <= 0:
        raise InvalidUserError(f"ID должен быть положительным. Получено: {ID}")
    return ID


class User:
    def __init__(self, username: str, age: int, ID: int):
        self.username = check_username(username)
        self.age = check_age(age)
        self.ID = check_ID(ID)

    def change_username(self, new_username: str):
        self.username = check_username(new_username)

    def change_age(self, new_age: int):
        self.age = check_age(new_age)

    def __str__(self):
        return f"Имя - {self.username}, возраст - {self.age}, ID - {self.ID}"