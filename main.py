import json
from user import User


def load_to_json(file):
    try:
        with open(file, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print("файл не найден")
        return {"users": []}
    except json.JSONDecodeError:
        print("файл поврежден или не является валидным")
        return {"users": []}


users = []

# data_json = load_to_json('data.json')
# users = User.load_users_json(data_json["users"])
users = User.load_users_xml('data.xml')
try:
    users.append(User("Bob", 12, 100))
except ValueError as error:
    print(error)


# users.append(User('Krabik', 12, 13))
# users.append(User('Cat', 17, 122))
