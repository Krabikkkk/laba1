import json
import xml.etree.ElementTree as ET
from user import User
from movie import Movie
from genre import Genre
from payment import Payment
from review import Review
from subscription import Subscription
from viewing import Viewing
from watchlist import Watchlist
from watchHistory import WatchHistory
from collection import Collection
from exceptions import (
    InvalidUserError, InvalidMovieError, InvalidGenreError, InvalidPaymentError,
    InvalidReviewError, InvalidSubscriptionError, InvalidViewingError,
    InvalidWatchlistError, InvalidWatchHistoryError, InvalidCollectionError
)

def load_data_from_json(filename: str):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f" Файл {filename} не найден. Создаём пустые данные.")
        return [], [], [], [], [], [], [], [], [], []
    except json.JSONDecodeError as e:
        print(f" Файл {filename} повреждён: {e}")
        return [], [], [], [], [], [], [], [], [], []

    users = []
    for i, user_data in enumerate(data.get("users", []), 1):
        try:
            user = User(
                username=user_data["username"],
                age=user_data["age"],
                ID=user_data["ID"]
            )
            users.append(user)
        except (InvalidUserError, KeyError) as e:
            print(f" Ошибка в пользователе #{i}: {e}")

    movies = []
    for i, movie_data in enumerate(data.get("movies", []), 1):
        try:
            movie = Movie(
                title=movie_data["title"],
                genre=movie_data["genre"],
                duration=movie_data["duration"],
                ID=movie_data["ID"]
            )
            movies.append(movie)
        except (InvalidMovieError, KeyError) as e:
            print(f" Ошибка в фильме #{i}: {e}")

    genres = []
    for i, genre_data in enumerate(data.get("genres", []), 1):
        try:
            genre = Genre(
                name=genre_data["name"],
                description=genre_data.get("description"),
                ID=genre_data["ID"]
            )
            genres.append(genre)
        except (InvalidGenreError, KeyError) as e:
            print(f" Ошибка в жанре #{i}: {e}")

    payments = []
    for i, payment_data in enumerate(data.get("payments", []), 1):
        try:
            payment = Payment(
                user_ID=payment_data["user_ID"],
                amount=payment_data["amount"],
                date=payment_data["date"],
                status=payment_data["status"]
            )
            payments.append(payment)
        except (InvalidPaymentError, KeyError) as e:
            print(f" Ошибка в платеже #{i}: {e}")

    reviews = []
    for i, review_data in enumerate(data.get("reviews", []), 1):
        try:
            review = Review(
                user_id=review_data["user_id"],
                movie_id=review_data["movie_id"],
                rating=review_data["rating"]
            )
            reviews.append(review)
        except (InvalidReviewError, KeyError) as e:
            print(f" Ошибка в отзыве #{i}: {e}")

    subscriptions = []
    for i, sub_data in enumerate(data.get("subscriptions", []), 1):
        try:
            subscription = Subscription(
                type_sub=sub_data["type_sub"],
                start_date=sub_data["start_date"],
                end_date=sub_data["end_date"],
                user_ID=sub_data["user_ID"]
            )
            subscriptions.append(subscription)
        except (InvalidSubscriptionError, KeyError) as e:
            print(f" Ошибка в подписке #{i}: {e}")

    viewings = []
    for i, viewing_data in enumerate(data.get("viewings", []), 1):
        try:
            viewing = Viewing(
                user_id=viewing_data["user_id"],
                movie_id=viewing_data["movie_id"],
                watch_time=viewing_data["watch_time"]
            )
            viewings.append(viewing)
        except (InvalidViewingError, KeyError) as e:
            print(f" Ошибка в просмотре #{i}: {e}")

    watchlists = []
    for i, wl_data in enumerate(data.get("watchlists", []), 1):
        try:
            watchlist = Watchlist(
                user_id=wl_data["user_id"],
                movie_ids=wl_data["movie_ids"],
                name=wl_data["name"]
            )
            watchlists.append(watchlist)
        except (InvalidWatchlistError, KeyError) as e:
            print(f" Ошибка в списке к просмотру #{i}: {e}")

    watch_histories = []
    for i, wh_data in enumerate(data.get("watch_histories", []), 1):
        try:
            watch_history = WatchHistory(
                user_id=wh_data["user_id"],
                movie_ids=wh_data["movie_ids"]
            )
            watch_histories.append(watch_history)
        except (InvalidWatchHistoryError, KeyError) as e:
            print(f" Ошибка в истории просмотров #{i}: {e}")

    collections = []
    for i, col_data in enumerate(data.get("collections", []), 1):
        try:
            collection = Collection(
                ID=col_data["ID"],
                name=col_data["name"],
                movie_ids=col_data["movie_ids"]
            )
            collections.append(collection)
        except (InvalidCollectionError, KeyError) as e:
            print(f" Ошибка в подборке #{i}: {e}")

    return users, movies, genres, payments, reviews, subscriptions, viewings, watchlists, watch_histories, collections

def load_data_from_xml(filename: str):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
    except FileNotFoundError:
        print(f" Файл {filename} не найден. Создаём пустые данные.")
        return [], [], [], [], [], [], [], [], [], []
    except ET.ParseError as e:
        print(f" Файл {filename} повреждён: {e}")
        return [], [], [], [], [], [], [], [], [], []

    users = []
    for i, user_elem in enumerate(root.findall("user"), 1):
        try:
            username = user_elem.find("username").text
            age = user_elem.find("age").text
            ID = user_elem.find("ID").text
            user = User(username=username, age=age, ID=ID)
            users.append(user)
        except (InvalidUserError, AttributeError) as e:
            print(f" Ошибка в пользователе #{i} (XML): {e}")

    movies = []
    for i, movie_elem in enumerate(root.findall("movie"), 1):
        try:
            title = movie_elem.find("title").text
            genre = movie_elem.find("genre").text
            duration = movie_elem.find("duration").text
            ID = movie_elem.find("ID").text
            movie = Movie(title=title, genre=genre, duration=duration, ID=ID)
            movies.append(movie)
        except (InvalidMovieError, AttributeError) as e:
            print(f" Ошибка в фильме #{i} (XML): {e}")

    genres = []
    for i, genre_elem in enumerate(root.findall("genre"), 1):
        try:
            name = genre_elem.find("name").text
            description_elem = genre_elem.find("description")
            description = description_elem.text if description_elem is not None else None
            ID = genre_elem.find("ID").text
            genre = Genre(name=name, description=description, ID=ID)
            genres.append(genre)
        except (InvalidGenreError, AttributeError) as e:
            print(f" Ошибка в жанре #{i} (XML): {e}")

    payments = []
    for i, payment_elem in enumerate(root.findall("payment"), 1):
        try:
            user_ID = payment_elem.find("user_ID").text
            amount = payment_elem.find("amount").text
            date = payment_elem.find("date").text
            status = payment_elem.find("status").text
            payment = Payment(user_ID=user_ID, amount=amount, date=date, status=status)
            payments.append(payment)
        except (InvalidPaymentError, AttributeError) as e:
            print(f" Ошибка в платеже #{i} (XML): {e}")

    reviews = []
    for i, review_elem in enumerate(root.findall("review"), 1):
        try:
            user_id = review_elem.find("user_id").text
            movie_id = review_elem.find("movie_id").text
            rating = review_elem.find("rating").text
            review = Review(user_id=user_id, movie_id=movie_id, rating=rating)
            reviews.append(review)
        except (InvalidReviewError, AttributeError) as e:
            print(f" Ошибка в отзыве #{i} (XML): {e}")

    subscriptions = []
    for i, sub_elem in enumerate(root.findall("subscription"), 1):
        try:
            type_sub = sub_elem.find("type_sub").text
            start_date = sub_elem.find("start_date").text
            end_date = sub_elem.find("end_date").text
            user_ID = sub_elem.find("user_ID").text
            subscription = Subscription(type_sub=type_sub, start_date=start_date, end_date=end_date, user_ID=user_ID)
            subscriptions.append(subscription)
        except (InvalidSubscriptionError, AttributeError) as e:
            print(f" Ошибка в подписке #{i} (XML): {e}")

    viewings = []
    for i, viewing_elem in enumerate(root.findall("viewing"), 1):
        try:
            user_id = viewing_elem.find("user_id").text
            movie_id = viewing_elem.find("movie_id").text
            watch_time = viewing_elem.find("watch_time").text
            viewing = Viewing(user_id=user_id, movie_id=movie_id, watch_time=watch_time)
            viewings.append(viewing)
        except (InvalidViewingError, AttributeError) as e:
            print(f" Ошибка в просмотре #{i} (XML): {e}")

    watchlists = []
    for i, wl_elem in enumerate(root.findall("watchlist"), 1):
        try:
            user_id = wl_elem.find("user_id").text
            name = wl_elem.find("name").text
            movie_ids = [mid.text for mid in wl_elem.find("movie_ids")]
            watchlist = Watchlist(user_id=user_id, movie_ids=movie_ids, name=name)
            watchlists.append(watchlist)
        except (InvalidWatchlistError, AttributeError) as e:
            print(f" Ошибка в списке к просмотру #{i} (XML): {e}")

    watch_histories = []
    for i, wh_elem in enumerate(root.findall("watch_history"), 1):
        try:
            user_id = wh_elem.find("user_id").text
            movie_ids = [mid.text for mid in wh_elem.find("movie_ids")]
            watch_history = WatchHistory(user_id=user_id, movie_ids=movie_ids)
            watch_histories.append(watch_history)
        except (InvalidWatchHistoryError, AttributeError) as e:
            print(f" Ошибка в истории просмотров #{i} (XML): {e}")

    collections = []
    for i, col_elem in enumerate(root.findall("collection"), 1):
        try:
            ID = col_elem.find("ID").text
            name = col_elem.find("name").text
            movie_ids = [mid.text for mid in col_elem.find("movie_ids")]
            collection = Collection(ID=ID, name=name, movie_ids=movie_ids)
            collections.append(collection)
        except (InvalidCollectionError, AttributeError) as e:
            print(f" Ошибка в подборке #{i} (XML): {e}")

    return users, movies, genres, payments, reviews, subscriptions, viewings, watchlists, watch_histories, collections

def save_data_to_json(users, movies, genres, payments, reviews, subscriptions, viewings, watchlists, watch_histories, collections, filename):
    data = {
        "users": [u.__dict__ for u in users],
        "movies": [m.__dict__ for m in movies],
        "genres": [g.__dict__ for g in genres],
        "payments": [p.__dict__ for p in payments],
        "reviews": [r.__dict__ for r in reviews],
        "subscriptions": [s.__dict__ for s in subscriptions],
        "viewings": [v.__dict__ for v in viewings],
        "watchlists": [wl.__dict__ for wl in watchlists],
        "watch_histories": [wh.__dict__ for wh in watch_histories],
        "collections": [c.__dict__ for c in collections]
    }
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def save_data_to_xml(users, movies, genres, payments, reviews, subscriptions, viewings, watchlists, watch_histories, collections, filename):
    root = ET.Element("cinema")

    for user in users:
        user_elem = ET.SubElement(root, "user")
        ET.SubElement(user_elem, "username").text = user.username
        ET.SubElement(user_elem, "age").text = str(user.age)
        ET.SubElement(user_elem, "ID").text = str(user.ID)

    for movie in movies:
        movie_elem = ET.SubElement(root, "movie")
        ET.SubElement(movie_elem, "title").text = movie.title
        ET.SubElement(movie_elem, "genre").text = movie.genre
        ET.SubElement(movie_elem, "duration").text = str(movie.duration)
        ET.SubElement(movie_elem, "ID").text = str(movie.ID)

    for genre in genres:
        genre_elem = ET.SubElement(root, "genre")
        ET.SubElement(genre_elem, "name").text = genre.name
        if genre.description is not None:
            ET.SubElement(genre_elem, "description").text = genre.description
        ET.SubElement(genre_elem, "ID").text = str(genre.ID)

    for payment in payments:
        payment_elem = ET.SubElement(root, "payment")
        ET.SubElement(payment_elem, "user_ID").text = str(payment.user_ID)
        ET.SubElement(payment_elem, "amount").text = str(payment.amount)
        ET.SubElement(payment_elem, "date").text = payment.date
        ET.SubElement(payment_elem, "status").text = payment.status

    for review in reviews:
        review_elem = ET.SubElement(root, "review")
        ET.SubElement(review_elem, "user_id").text = str(review.user_id)
        ET.SubElement(review_elem, "movie_id").text = str(review.movie_id)
        ET.SubElement(review_elem, "rating").text = str(review.rating)

    for subscription in subscriptions:
        sub_elem = ET.SubElement(root, "subscription")
        ET.SubElement(sub_elem, "type_sub").text = subscription.type_sub
        ET.SubElement(sub_elem, "start_date").text = subscription.start_date
        ET.SubElement(sub_elem, "end_date").text = subscription.end_date
        ET.SubElement(sub_elem, "user_ID").text = str(subscription.user_ID)

    for viewing in viewings:
        viewing_elem = ET.SubElement(root, "viewing")
        ET.SubElement(viewing_elem, "user_id").text = str(viewing.user_id)
        ET.SubElement(viewing_elem, "movie_id").text = str(viewing.movie_id)
        ET.SubElement(viewing_elem, "watch_time").text = viewing.watch_time

    for watchlist in watchlists:
        wl_elem = ET.SubElement(root, "watchlist")
        ET.SubElement(wl_elem, "user_id").text = str(watchlist.user_id)
        ET.SubElement(wl_elem, "name").text = watchlist.name
        movie_ids_elem = ET.SubElement(wl_elem, "movie_ids")
        for mid in watchlist.movie_ids:
            mid_elem = ET.SubElement(movie_ids_elem, "movie_id")
            mid_elem.text = str(mid)

    for watch_history in watch_histories:
        wh_elem = ET.SubElement(root, "watch_history")
        ET.SubElement(wh_elem, "user_id").text = str(watch_history.user_id)
        movie_ids_elem = ET.SubElement(wh_elem, "movie_ids")
        for mid in watch_history.movie_ids:
            mid_elem = ET.SubElement(movie_ids_elem, "movie_id")
            mid_elem.text = str(mid)

    for collection in collections:
        col_elem = ET.SubElement(root, "collection")
        ET.SubElement(col_elem, "ID").text = str(collection.ID)
        ET.SubElement(col_elem, "name").text = collection.name
        movie_ids_elem = ET.SubElement(col_elem, "movie_ids")
        for mid in collection.movie_ids:
            mid_elem = ET.SubElement(movie_ids_elem, "movie_id")
            mid_elem.text = str(mid)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def delete_user_by_id(users, user_id):
    for i, user in enumerate(users):
        if user.ID == user_id:
            users.pop(i)
            return True
    return False


def delete_review_by_user_and_movie(reviews, user_id, movie_id):
    for i, review in enumerate(reviews):
        if review.user_id == user_id and review.movie_id == movie_id:
            reviews.pop(i)
            return True
    return False


def delete_movie_from_watchlist(watchlists, user_id, movie_id):
    for watchlist in watchlists:
        if watchlist.user_id == user_id:
            if movie_id in watchlist.movie_ids:
                watchlist.movie_ids.remove(movie_id)
                return True
    return False

def remove_movie_from_watchlist(watchlists, user_id, movie_id):
    for watchlist in watchlists:
        if watchlist.user_id == user_id:
            if movie_id in watchlist.movie_ids:
                watchlist.movie_ids.remove(movie_id)
                return True
    return False


if __name__ == '__main__':
    #users, movies, genres, payments, reviews, subscriptions, viewings, watchlists, watch_histories, collections = load_data_from_xml("data.xml")
    users, movies, genres, payments, reviews, subscriptions, viewings, watchlists, watch_histories, collections = load_data_from_json("data.json")
    print(f"Загружено пользователей: {len(users)}")
    for user in users:
        print(user)

    try:
        user = User("Steve", "abc", 133)
    except InvalidUserError as e:
        print("Ошибка создания пользователя:", e)
