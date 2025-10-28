import xml.etree.ElementTree as ET


class User:
    username: str
    age: int
    ID: int

    def __init__(self, username:str, age:int, ID:int):
        if not username or not isinstance(username, str):
            raise ValueError("Имя пользователя должно быть непустой строкой")
        if not isinstance(age, int) or age < 6 or age > 100:
            raise ValueError("Возраст должен быть целым числом от 6 до 100")
        if not isinstance(ID, int) or ID <= 0:
            raise ValueError("ID должен быть положительным целым числом")

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
    def delete_user(cls,users:list, ID_delete:int) -> int:
        num_of_user = 0
        for user in users:
            if user.ID == ID_delete:
                print("Пользователь с ID -",user.ID, "удален")
                return num_of_user
            num_of_user += 1
        print("Пользователя с таким ID не существует")

    def change_username(self, value:str):
        self.username = str(value)

    def change_age(self, value:int):
        self.age = int(value)


