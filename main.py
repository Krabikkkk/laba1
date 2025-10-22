import json
from user import User


def load_to_json(file):
    with open(file, 'r', encoding='UTF-8') as f:
        data = json.load(f)
    return data



users = []

# data_json = load_to_json('data.json')
# users = User.load_users_json(data_json["users"])
users = User.load_users_xml('data.xml')



# users.append(User('Krabik', 12, 13))
# users.append(User('Cat', 17, 122))
for user in users:
    print(user.username)