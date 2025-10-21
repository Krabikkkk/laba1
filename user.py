import json


class User:
    username: str
    age: int
    ID: int

    def __init__(self, username:str, age:int, ID:int):
        self.username = username
        self.age = age
        self.ID = ID

    @classmethod
    def load_users(cls, data) -> list["User"]:
        users = []
        for user_data in data:
            user = cls(user_data["username"], user_data["age"], user_data["ID"])
            users.append(user)
        return users

    @classmethod
    def delete_user(cls,users, ID_delete) -> int:
        num_of_user = 0
        for user in users:
            if user.ID == ID_delete:
                print("Пользователь с ID -",user.ID, "удален")
                return num_of_user
            num_of_user += 1
        print("Пользователя с таким ID не существует")
    #ошибка если передать значение больше массива - исправить

    def change_username(self, value):
        self.username = str(value)

    def change_age(self, value):
        self.age = int(value)

    def save_to_json(self):
        pass