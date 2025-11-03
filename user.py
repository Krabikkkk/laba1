import xml.etree.ElementTree as ET



def check_username(username, num_of_user=None):
    if username is None or username == "" or not isinstance(username, str):
        if num_of_user is not None:
            print(f"имя пользователя {num_of_user} неверное")
        else:
            print("неверное имя пользователя")
        return False
    return True


def check_age(age, num_of_user=None):
    if age is None:
        if num_of_user is not None:
            print(f"отсутствует поле age для пользователя {num_of_user}")
        else:
            print("отсутствует поле age")
        return False, None
    try:
        age = int(age)
    except (ValueError, TypeError) as error:
        if num_of_user is not None:
            print(f"для пользователя {num_of_user} было передано неверное значение возраста: {error}")
        else:
            print(f"неверное значение возраста: {error}")
        return False, None
    if not (6 <= age <= 100):
        if num_of_user is not None:
            print(f"возраст пользователя {num_of_user} должен быть от 6 до 100, ваш возраст - {age}")
        else:
            print(f"возраст должен быть от 6 до 100, ваш возраст - {age}")
        return False, None
    return True, age

def check_ID(ID, num_of_user=None):
    if ID is None:
        if num_of_user is not None:
            print(f"отсутствует поле ID для пользователя {num_of_user}")
        else:
            print("отсутствует поле ID")
        return False, None
    try:
        ID_int = int(ID)
    except (ValueError, TypeError) as error:
        if num_of_user is not None:
            print(f"для пользователя {num_of_user} было передано неверное значение ID: {error}")
        else:
            print(f"неверное значение ID: {error}")
        return False, None
    if not (ID_int > 0):
        if num_of_user is not None:
            print(f"ID пользователя {num_of_user} должен быть больше 0, ваш ID {ID}")
        else:
            print(f"ID должен быть больше 0, ваш ID {ID}")
        return False, None
    return True, ID_int



class User:
    username: str
    age: int
    ID: int

    def __init__(self, username:str, age:int, ID:int):
        if not check_username(username):
            raise ValueError
        is_valid, age = check_age(age)
        if not is_valid:
            raise ValueError
        is_valid, ID = check_ID(ID)
        if not is_valid:
            raise ValueError

        self.username = username
        self.age = age
        self.ID = ID




    @classmethod
    def load_users_json(cls, data) -> list["User"]:
        users = []
        num_of_user = 0
        for user_data in data:
            num_of_user += 1
            username = user_data.get("username")
            if not check_username(username, num_of_user):
                continue
            age = user_data.get("age")
            is_valid, age =  check_age(age, num_of_user)
            if not is_valid:
                continue

            ID = user_data.get("ID")
            is_valid, ID = check_ID(ID, num_of_user)
            if not is_valid:
                continue
            try:
                user = cls(username, age, ID)
                users.append(user)

            except ValueError as error:
                print(f"ошибка при создании {num_of_user} пользователя {error}")
        return users

    @classmethod
    def load_users_xml(cls, file) -> list["User"]:
        users = []
        try:
            with open(file, 'r', encoding='UTF-8') as f:
                tree = ET.parse(f)
                root = tree.getroot()
                if root is None:
                    print("XML-файл пуст или не содержит корневого элемента")
                    return users
                for user_elem in root.findall("user"):
                    username_elem = user_elem.find("username")
                    if username_elem is None:
                        print("Пропущен тег <username>")
                        continue
                    username = username_elem.text
                    if not check_username(username):
                        continue
                    age_elem = user_elem.find("age")
                    if age_elem is None:
                        print("Пропущен тег <age>")
                        continue
                    age_text = age_elem.text
                    is_valid_age, age = check_age(age_text)
                    if not is_valid_age:
                        continue
                    id_elem = user_elem.find("ID")
                    if id_elem is None:
                        print("Пропущен тег <ID>")
                        continue
                    id_text = id_elem.text
                    is_valid_id, ID = check_ID(id_text)
                    if not is_valid_id:
                        continue
                    try:
                        user_obj = cls(username, age, ID)
                        users.append(user_obj)
                    except ValueError as e:
                        print(f"Ошибка валидации: {e}")
                        continue

        except FileNotFoundError:
            print(f"Файл '{file}' не найден")
        except ET.ParseError as e:
            print(f"Ошибка парсинга XML: {e}")
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")

        return users


    @classmethod
    def delete_user(cls,users:list, ID_delete:int):
        if not isinstance(users, list):
            print("ожидается список пользователей")
            return
        is_valid, ID_delete = check_ID(ID_delete)
        if not is_valid:
            return
        for i, user in enumerate(users):
            if user.ID == ID_delete:
                users.pop(i)
                print(f"Пользователь с ID - {user.ID} удален")
                return
        print(f"Пользователя с {ID_delete} ID не существует")
        return

    def change_username(self, username:str):
        if not check_username(username):
            return
        self.username = str(username)
        return

    def change_age(self, age:int):
        is_valid, age = check_age(age)
        if not is_valid:
            return
        self.age = int(age)
        return



    def __str__(self):
        return f"Имя - {self.username}, возраст -  {self.age}, ID - {self.ID}"

