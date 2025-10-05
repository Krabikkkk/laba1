class Playlist:
    name = None
    owner_id = None
    movie_ids = None

    def __init__(self, name, owner_id, movie_ids):
        self.name = name
        self.owner_id = owner_id
        self.movie_ids = movie_ids