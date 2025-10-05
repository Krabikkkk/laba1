class Viewing:
    user_id = None
    movie_id = None
    watch_time = None

    def __init__(self, user_id, movie_id, watch_time):
        self.user_id = user_id
        self.movie_id = movie_id
        self.watch_time = watch_time