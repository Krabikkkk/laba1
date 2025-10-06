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

    def create_user(self, username, age, ID):
        user = User(username, age, ID)
        self.users.append(user)
        return user


    def movie_create(self, title, genre, duration):
        movie = Movie(title, genre, duration)
        self.movies.append(movie)
        return movie

    def collection_create(self, name, films, ID):
        collection = Collection(name, films, ID)
        self.collections.append(collection)
        return collection

    def genre_create(self, name, description, ID):
        genre = Genre(name, description, ID)
        self.genres.append(genre)
        return genre

    def create_payment(self, amount, date, status):
        payment = Payment(amount, date, status)
        self.payments.append(payment)
        return payment

    def create_review(self, user_id, movie_id, rating):
        review = Review(user_id, movie_id, rating)
        self.reviews.append(review)
        return review

    def create_subscription(self, type_sub, start_date, end_date):
        subscription = Subscription(type_sub, start_date, end_date)
        self.subscriptions.append(subscription)
        return subscription

    def create_viewing(self, user_id, movie_id, watch_time):
        viewing = Viewing(user_id, movie_id, watch_time)
        self.viewings.append(viewing)
        return viewing

    def create_watch_history(self, name, movie_ids):
        watch_history = WatchHistory(name, movie_ids)
        self.watch_histories.append(watch_history)
        return watch_history

    def create_watchlist(self, user_id, movie_ids, name):
        watchlist = Watchlist(user_id, movie_ids, name)
        self.watchlists.append(watchlist)
        return watchlist