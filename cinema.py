from collection import Collection
from genre import Genre
from movie import Movie
from payment import Payment
from review import Review
from subscription import Subscription
from user import User
from viewing import Viewing
from watchHistory import WatchHistory
from watchlist import Watchlist
class Cinema:
    def __init__(self):
        self.users = []
        self.movies = []
        self.genres = []
        self.payments = []
        self.reviews = []
        self.subscriptions = []
        self.viewings = []
        self.watch_histories = []
        self.watchlists = []
        self.collections = []
