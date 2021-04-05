class Swap:

    def __init__(self, tx_id, user, from_token, to_token, from_token_amount, to_token_amount, timestamp, protocol):
        self.user = user
        self.tx_id = tx_id
        self.from_token = from_token
        self.to_token = to_token
        self.from_token_amount = from_token_amount
        self.to_token_amount = to_token_amount
        self.timestamp = timestamp
        self.protocol = protocol

    def to_dict(self):
        borrow = {}
        for key, value in self.__dict__.items():
            borrow[key] = value
        return borrow
