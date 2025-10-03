class User:
    username = None
    age = None
    ID = None

    def set_data(self, username, age, ID):
        self.username = username
        self.age = age
        self.ID = ID


class Movie:
    title = None
    genre = None
    duration = None

    def set_data(self, title, genre, duration):
        self.title = title
        self.genre = genre
        self.duration = duration


class Subscription:
    type = None
    start_date = None
    end_date = None

    def set_data(self, type, start_date, end_date):
        self.type = type
        self.start_date = start_date
        self.end_date = end_date


class Genre:
    name = None
    description = None
    ID = None

    def set_data(self, name, description, ID):
        self.name = name
        self.description = description
        self.ID = ID


class Viewing:
    user_id = None
    movie_id = None
    watch_time = None

    def set_data(self, user_id, movie_id, watch_time):
        self.user_id = user_id
        self.movie_id = movie_id
        self.watch_time = watch_time


class Payment:
    amount = None
    date = None
    status = None

    def set_data(self, amount, date, status):
        self.amount = amount
        self.date = date
        self.status = status


class Review:
    user_id = None
    movie_id = None
    rating = None

    def set_data(self, user_id, movie_id, rating):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating


class Director:
    name = None
    birth_year = None
    ID = None

    def set_data(self, name, birth_year, ID):
        self.name = name
        self.birth_year = birth_year
        self.ID = ID


class Watchlist:
    user_id = None
    movie_ids = None
    name = None

    def set_data(self, user_id, movie_ids, name):
        self.user_id = user_id
        self.movie_ids = movie_ids
        self.name = name


class Playlist:
    name = None
    owner_id = None
    movie_ids = None

    def set_data(self, name, owner_id, movie_ids):
        self.name = name
        self.owner_id = owner_id
        self.movie_ids = movie_ids