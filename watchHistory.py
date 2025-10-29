class WatchHistory:
    user_ID = None
    movie_names = []
    movie_ids = []
    movie_genre = []

    def __init__(self, name, movie_ids):
        self.name = name
        self.movie_ids = movie_ids