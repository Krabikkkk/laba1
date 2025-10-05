class Watchlist:
    user_id = None
    movie_ids = None
    name = None

    def __init__(self, user_id, movie_ids, name):
        self.user_id = user_id
        self.movie_ids = movie_ids
        self.name = name