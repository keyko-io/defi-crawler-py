class User:

    def __init__(self, user_id, activeLoans, liquidations_count, protocol):
        self.user_id = user_id
        self.active_loans = activeLoans
        self.liquidations_count = liquidations_count
        self.protocol = protocol

    def to_dict(self):
        user = {}
        for key, value in self.__dict__.items():
            user[key] = value
        return user
