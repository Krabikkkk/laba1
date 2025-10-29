class Collection:
    name_of_collection = None
    films = []
    ID = []

    def __init__(self, name_of_collection, films, ID):
        self.name_of_collection = name_of_collection
        self.films = films
        self.ID = ID