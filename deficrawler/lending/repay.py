class Repay:

    def __init__(self, user, token, amount, timestamp, protocol):
        self.user = user
        self.token = token
        self.amount = amount
        self.timestamp = timestamp
        self.protocol = protocol

    def to_dict(self):
        repay = {}
        for key, value in self.__dict__.items():
            repay[key] = value
        return repay
