import xml.etree.ElementTree as ET


def check_genre_name(name, num=None):
    if name is None or name == "" or not isinstance(name, str):
        if num is not None:
            print(f"Название жанра {num} не может быть пустым")
        else:
            print("Название жанра не может быть пустым")
        return False
    return True


def check_genre_description(description, num=None):
    if description is not None and (not isinstance(description, str) or description == ""):
        if num is not None:
            print(f"Описание жанра {num} должно быть непустой строкой или отсутствовать")
        else:
            print("Описание жанра должно быть непустой строкой или отсутствовать")
        return False
    return True


def check_genre_id(genre_id, num=None):
    if genre_id is None:
        if num is not None:
            print(f"Отсутствует поле ID для жанра {num}")
        else:
            print("Отсутствует поле ID")
        return False, None
    try:
        gid = int(genre_id)
    except (ValueError, TypeError) as error:
        if num is not None:
            print(f"Для жанра {num} передано неверное значение ID: {error}")
        else:
            print(f"Неверное значение ID: {error}")
        return False, None
    if gid <= 0:
        if num is not None:
            print(f"ID жанра {num} должен быть больше 0, ваш ID: {genre_id}")
        else:
            print(f"ID должен быть больше 0, ваш ID: {genre_id}")
        return False, None
    return True, gid


class Genre:
    name: str
    description: str
    ID: int

    def __init__(self, name: str, description: str, ID: int):
        if not check_genre_name(name):
            raise ValueError
        if not check_genre_description(description):
            raise ValueError
        is_valid, ID = check_genre_id(ID)
        if not is_valid:
            raise ValueError

        self.name = name
        self.description = description
        self.ID = ID

    @classmethod
    def load_genres_json(cls, data) -> list["Genre"]:
        genres = []
        num_of_genre = 0
        for genre_data in data:
            num_of_genre += 1
            name = genre_data.get("name")
            if not check_genre_name(name, num_of_genre):
                continue
            description = genre_data.get("description")
            if not check_genre_description(description, num_of_genre):
                continue
            ID = genre_data.get("ID")
            is_valid, ID = check_genre_id(ID, num_of_genre)
            if not is_valid:
                continue
            try:
                genre = cls(name, description, ID)
                genres.append(genre)
            except ValueError as error:
                print(f"Ошибка при создании {num_of_genre} жанра: {error}")
        return genres

    @classmethod
    def load_genres_xml(cls, file) -> list["Genre"]:
        genres = []
        try:
            with open(file, 'r', encoding='UTF-8') as f:
                tree = ET.parse(f)
                root = tree.getroot()
                if root is None:
                    print("XML-файл пуст или не содержит корневого элемента")
                    return genres
                for i, genre_elem in enumerate(root.findall("genre"), 1):
                    name_elem = genre_elem.find("name")
                    if name_elem is None:
                        print(f"Пропущен тег <name> у жанра {i}")
                        continue
                    name = name_elem.text
                    if not check_genre_name(name, i):
                        continue

                    desc_elem = genre_elem.find("description")
                    description = desc_elem.text if desc_elem is not None else None
                    if not check_genre_description(description, i):
                        continue

                    id_elem = genre_elem.find("ID")
                    if id_elem is None:
                        print(f"Пропущен тег <ID> у жанра {i}")
                        continue
                    id_text = id_elem.text
                    is_valid_id, ID = check_genre_id(id_text, i)
                    if not is_valid_id:
                        continue

                    try:
                        genre_obj = cls(name, description, ID)
                        genres.append(genre_obj)
                    except ValueError as e:
                        print(f"Ошибка валидации жанра {i}: {e}")
                        continue

        except FileNotFoundError:
            print(f"Файл '{file}' не найден")
        except ET.ParseError as e:
            print(f"Ошибка парсинга XML: {e}")
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")

        return genres

    def __str__(self):
        desc = f", описание: {self.description}" if self.description else ""
        return f"Жанр - {self.name}{desc}, ID - {self.ID}"