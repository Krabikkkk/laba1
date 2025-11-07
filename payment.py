from exceptions import InvalidPaymentError

class Payment:

    @staticmethod
    def check_payment_amount(amount):
        if amount is None:
            raise InvalidPaymentError("Сумма платежа не указана")
        try:
            amount = float(amount)
        except (ValueError, TypeError):
            raise InvalidPaymentError("Сумма платежа должна быть числом")
        if amount <= 0:
            raise InvalidPaymentError(f"Сумма платежа должна быть положительной. Получено: {amount}")
        return amount

    @staticmethod
    def check_payment_date(date):
        if date is None:
            raise InvalidPaymentError("Дата платежа не указана")
        if not isinstance(date, str):
            raise InvalidPaymentError("Дата платежа должна быть строкой")
        if date.strip() == "":
            raise InvalidPaymentError("Дата платежа не может быть пустой")
        return date.strip()

    @staticmethod
    def check_payment_status(status):
        if status is None:
            raise InvalidPaymentError("Статус платежа не указан")
        if not isinstance(status, str):
            raise InvalidPaymentError("Статус платежа должен быть строкой")
        valid_statuses = {"ожидает", "успешно", "отклонён", "возврат"}
        if status.strip().lower() not in valid_statuses:
            raise InvalidPaymentError(
                f"Недопустимый статус платежа: '{status}'. "
                f"Допустимые значения: {', '.join(valid_statuses)}"
            )
        return status.strip().lower()

    @staticmethod
    def check_ID(ID):
        if ID is None:
            raise InvalidPaymentError("Поле 'ID' не может быть пустым")
        try:
            ID = int(ID)
        except (ValueError, TypeError):
            raise InvalidPaymentError("ID должен быть целым числом")
        if ID <= 0:
            raise InvalidPaymentError(f"ID должен быть положительным. Получено: {ID}")
        return ID

    def __init__(self, user_ID: int, amount, date: str, status: str):
        self.user_ID = self.check_ID(user_ID)
        self.amount = self.check_payment_amount(amount)
        self.date = self.check_payment_date(date)
        self.status = self.check_payment_status(status)

    def __str__(self):
        return f"Платёж: пользователь {self.user_ID}, сумма {self.amount} руб, дата {self.date}, статус '{self.status}'"