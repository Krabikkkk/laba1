class Subscription:
    type = None
    start_date = None
    end_date = None

    def __init__(self, type, start_date, end_date):
        self.type = type
        self.start_date = start_date
        self.end_date = end_date