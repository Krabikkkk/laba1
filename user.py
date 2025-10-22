import xml.etree.ElementTree as ET


class User:
    username: str
    age: int
    ID: int

    def __init__(self, username:str, age:int, ID:int):
        self.username = username
        self.age = age
        self.ID = ID

    @classmethod
    def load_users_json(cls, data) -> list["User"]:
        users = []
        for user_data in data:
            user = cls(user_data["username"], user_data["age"], user_data["ID"])
            users.append(user)
        return users

    @classmethod
    def load_users_xml(cls, file)  -> list["User"]:
        users = []
        with open(file, 'r', encoding='UTF-8') as f:
            tree = ET.parse(f)
            data = tree.getroot()
            for user in data.findall("user"):
                username = user.find("username").text
                age = int(user.find("age").text)
                ID = int(user.find("ID").text)
                user_obj = cls(username, age, ID)
                users.append(user_obj)
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


