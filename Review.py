class Review:
    user_id = None
    movie_id = None
    rating = None

    def __init__(self, user_id, movie_id, rating):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating