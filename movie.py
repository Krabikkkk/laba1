import xml.etree.ElementTree as ET
def check_movie_title(title, num=None):
    if not isinstance(title, str) or not title.strip():
        if num is not None:
            print(f"Название фильма {num} не может быть пустым")
        else:
            print("Название фильма не может быть пустым")
        return False
    return True

def check_movie_genre(genre, num=None):
    if not isinstance(genre, str) or not genre.strip():
        if num is not None:
            print(f"Жанр фильма {num} не может быть пустым")
        else:
            print("Жанр фильма не может быть пустым")
        return False
    return True

def check_movie_duration(duration, num=None):
    if duration is None:
        if num is not None:
            print(f"Длительность фильма {num} отсутствует")
        else:
            print("Длительность фильма отсутствует")
        return False, None
    try:
        dur = int(duration)
    except (ValueError, TypeError):
        if num is not None:
            print(f"Длительность фильма {num} должна быть числом")
        else:
            print("Длительность фильма должна быть числом")
        return False, None
    if dur <= 0:
        if num is not None:
            print(f"Длительность фильма {num} должна быть положительной")
        else:
            print("Длительность фильма должна быть положительной")
        return False, None
    return True, dur

def check_movie_id(movie_id, num=None):
    if movie_id is None:
        if num is not None:
            print(f"ID фильма {num} отсутствует")
        else:
            print("ID фильма отсутствует")
        return False, None
    try:
        mid = int(movie_id)
    except (ValueError, TypeError):
        if num is not None:
            print(f"ID фильма {num} должен быть числом")
        else:
            print("ID фильма должен быть числом")
        return False, None
    if mid <= 0:
        if num is not None:
            print(f"ID фильма {num} должен быть положительным")
        else:
            print("ID фильма должен быть положительным")
        return False, None
    return True, mid


class Movie:
    def __init__(self, title, genre, duration, ID):
        if not check_movie_title(title):
            raise ValueError
        if not check_movie_genre(genre):
            raise ValueError
        is_valid, duration = check_movie_duration(duration)
        if not is_valid:
            raise ValueError
        is_valid, ID = check_movie_id(ID)
        if not is_valid:
            raise ValueError
        self.title = title
        self.genre = genre
        self.duration = duration
        self.ID = ID

    @classmethod
    def load_movies_json(cls, data):
        movies = []
        num = 0
        for item in data:
            num += 1
            title = item.get("title")
            if not check_movie_title(title, num):
                continue
            genre = item.get("genre")
            if not check_movie_genre(genre, num):
                continue
            duration = item.get("duration")
            is_valid, duration = check_movie_duration(duration, num)
            if not is_valid:
                continue
            ID = item.get("ID")
            is_valid, ID = check_movie_id(ID, num)
            if not is_valid:
                continue
            try:
                movie = cls(title, genre, duration, ID)
                movies.append(movie)
            except ValueError as e:
                print(f"Ошибка при создании фильма {num}: {e}")
        return movies

    @classmethod
    def load_movies_xml(cls, file):
        movies = []
        try:
            with open(file, 'r', encoding='UTF-8') as f:
                tree = ET.parse(f)
                root = tree.getroot()
                for i, elem in enumerate(root.findall("movie"), 1):
                    title = elem.find("title").text if elem.find("title") is not None else None
                    genre = elem.find("genre").text if elem.find("genre") is not None else None
                    duration = elem.find("duration").text if elem.find("duration") is not None else None
                    ID = elem.find("ID").text if elem.find("ID") is not None else None

                    if not check_movie_title(title, i):
                        continue
                    if not check_movie_genre(genre, i):
                        continue
                    is_valid, duration = check_movie_duration(duration, i)
                    if not is_valid:
                        continue
                    is_valid, ID = check_movie_id(ID, i)
                    if not is_valid:
                        continue

                    try:
                        movie = cls(title, genre, duration, ID)
                        movies.append(movie)
                    except ValueError as e:
                        print(f"Ошибка при создании фильма {i}: {e}")
        except FileNotFoundError:
            print(f"Файл '{file}' не найден")
        except ET.ParseError as e:
            print(f"Ошибка парсинга XML: {e}")
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")
        return movies

    def __str__(self):
        return f"{self.title} ({self.genre}, {self.duration} мин), {self.ID} - ID"
