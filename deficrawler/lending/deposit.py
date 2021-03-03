class Deposit:

    def __init__(self, user, token, amount, timestamp, protocol):
        self.user = user
        self.token = token
        self.amount = amount
        self.timestamp = timestamp
        self.protocol = protocol

    def to_dict(self):
        deposit = {}
        for key, value in self.__dict__.items():
            deposit[key] = value
        return deposit
