class Payment:
    amount = None
    date = None
    status = None

    def __init__(self, amount, date, status):
        self.amount = amount
        self.date = date
        self.status = status