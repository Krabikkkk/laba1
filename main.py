import json
from user import User


def load_to_json(file):
    with open(file, 'r', encoding='UTF-8') as f:
        data = json.load(f)
    return data

users = []

data = load_to_json('1.json')
users = User.load_users(data["users"])

users[0].change_username(input())

# users.append(User('Krabik', 12, 13))
# users.append(User('Cat', 17, 122))
for user in users:
    print(user.username)