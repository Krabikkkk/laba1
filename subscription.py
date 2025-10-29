class Subscription:
    type_sub = None
    user_ID = None
    start_date = None
    end_date = None

    def __init__(self, type_sub, start_date, end_date, user_ID):
        self.type_sub = type_sub
        self.start_date = start_date
        self.end_date = end_date
        self.user_ID = user_ID