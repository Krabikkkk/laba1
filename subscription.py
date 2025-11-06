from exceptions import InvalidSubscriptionError


def check_subscription_user_id(user_id):
    if user_id is None:
        raise InvalidSubscriptionError("ID пользователя не указан")
    try:
        user_id = int(user_id)
    except (ValueError, TypeError):
        raise InvalidSubscriptionError("ID пользователя должен быть целым числом")
    if user_id <= 0:
        raise InvalidSubscriptionError(f"ID пользователя должен быть положительным. Получено: {user_id}")
    return user_id


def check_subscription_type(type_sub):
    if type_sub is None:
        raise InvalidSubscriptionError("Тип подписки не указан")
    if not isinstance(type_sub, str):
        raise InvalidSubscriptionError("Тип подписки должен быть строкой")
    valid_types = {"basic", "premium", "vip"}
    if type_sub.strip().lower() not in valid_types:
        raise InvalidSubscriptionError(
            f"Недопустимый тип подписки: '{type_sub}'. "
            f"Допустимые значения: {', '.join(valid_types)}"
        )
    return type_sub.strip().lower()


def check_subscription_date(date, field_name="дата"):
    if date is None:
        raise InvalidSubscriptionError(f"{field_name.capitalize()} не указана")
    if not isinstance(date, str):
        raise InvalidSubscriptionError(f"{field_name.capitalize()} должна быть строкой")
    if date.strip() == "":
        raise InvalidSubscriptionError(f"{field_name.capitalize()} не может быть пустой")
    return date.strip()


class Subscription:
    def __init__(self, type_sub: str, start_date: str, end_date: str, user_ID: int):
        self.user_ID = check_subscription_user_id(user_ID)
        self.type_sub = check_subscription_type(type_sub)
        self.start_date = check_subscription_date(start_date, "дата начала")
        self.end_date = check_subscription_date(end_date, "дата окончания")

    def __str__(self):
        return (f"Подписка: пользователь {self.user_ID}, тип '{self.type_sub}', "
                f"с {self.start_date} по {self.end_date}")