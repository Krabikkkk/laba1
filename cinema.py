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
import json


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

    def create_movie(self, title, genre, duration):
        movie = Movie(title, genre, duration)
        self.movies.append(movie)
        return movie

    def create_collection(self, name, films, ID):
        collection = Collection(name, films, ID)
        self.collections.append(collection)
        return collection

    def create_genre(self, name, description, ID):
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

    def load_json_file(self, data):
        with open("1.json", "r", encoding="UTF-8") as file:
            data = json.load(file)

            for user_data in data.get("users", []):
                self.create_user(
                    username = user_data["username"],
                    age=user_data["age"],
                    ID = user_data["ID"]
                )

            for movie_data in data.get("movies", []):
                self.create_movie(
                    title=movie_data["title"],
                    genre=movie_data["genre"],
                    duration=movie_data["duration"]
                )

            for collection_data in data.get("collections", []):
                self.create_collection(
                    name=collection_data["name"],
                    films=collection_data["films"],
                    ID=collection_data["ID"]
                )

            for genre_data in data.get("genres", []):
                self.create_genre(
                    name=genre_data["name"],
                    description=genre_data["description"],
                    ID=genre_data["ID"]
                )

            for payment_data in data.get("payments", []):
                self.create_payment(
                    amount=payment_data["amount"],
                    date=payment_data["date"],
                    status=payment_data["status"]
                )

            for review_data in data.get("reviews", []):
                self.create_review(
                    user_id=review_data["user_id"],
                    movie_id=review_data["movie_id"],
                    rating=review_data["rating"]
                )

            for subscription_data in data.get("subscriptions", []):
                self.create_subscription(
                    type_sub=subscription_data["type_sub"],
                    start_date=subscription_data["start_date"],
                    end_date=subscription_data["end_date"]
                )

            for viewing_data in data.get("viewings", []):
                self.create_viewing(
                    user_id=viewing_data["user_id"],
                    movie_id=viewing_data["movie_id"],
                    watch_time=viewing_data["watch_time"]
                )

            for watch_history_data in data.get("watch_histories", []):
                self.create_watch_history(
                    name=watch_history_data["name"],
                    movie_ids=watch_history_data["movie_ids"]
                )

            for watchlist_data in data.get("watchlists", []):
                self.create_watchlist(
                    user_id=watchlist_data["user_id"],
                    movie_ids=watchlist_data["movie_ids"],
                    name=watchlist_data["name"]
                )


    def delete_obj_of_cinema(self, section, num_of_section):
        section_delete = getattr(self, section)
        section_delete.pop(num_of_section)
        return self

    def change_obj_of_cinema(self, section, num_of_section, object_data, new_object_data):
        pass