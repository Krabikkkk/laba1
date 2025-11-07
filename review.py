from exceptions import InvalidReviewError

class Review:

    @staticmethod
    def check_review_user_id(user_id):
        if user_id is None:
            raise InvalidReviewError("ID пользователя не указан")
        try:
            user_id = int(user_id)
        except (ValueError, TypeError):
            raise InvalidReviewError("ID пользователя должен быть целым числом")
        if user_id <= 0:
            raise InvalidReviewError(f"ID пользователя должен быть положительным. Получено: {user_id}")
        return user_id

    @staticmethod
    def check_review_movie_id(movie_id):
        if movie_id is None:
            raise InvalidReviewError("ID фильма не указан")
        try:
            movie_id = int(movie_id)
        except (ValueError, TypeError):
            raise InvalidReviewError("ID фильма должен быть целым числом")
        if movie_id <= 0:
            raise InvalidReviewError(f"ID фильма должен быть положительным. Получено: {movie_id}")
        return movie_id

    @staticmethod
    def check_review_rating(rating):
        if rating is None:
            raise InvalidReviewError("Рейтинг не указан")
        try:
            rating = int(rating)
        except (ValueError, TypeError):
            raise InvalidReviewError("Рейтинг должен быть целым числом")
        if not (0 <= rating <= 10):
            raise InvalidReviewError(f"Рейтинг должен быть от 0 до 10. Получено: {rating}")
        return rating

    def __init__(self, user_id: int, movie_id: int, rating: float):
        self.user_id = self.check_review_user_id(user_id)
        self.movie_id = self.check_review_movie_id(movie_id)
        self.rating = self.check_review_rating(rating)

    def __str__(self):
        return f"Отзыв: пользователь {self.user_id} → фильм {self.movie_id}, рейтинг {self.rating}/10"