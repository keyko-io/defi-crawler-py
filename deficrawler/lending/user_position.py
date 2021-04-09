class UserPosition:

    def __init__(self, user_id, symbol, debt_amount, collateral_amount, protocol):
        self.user_id = user_id
        self.symbol = symbol
        self.debt_amount = debt_amount
        self.collateral_amount = collateral_amount
        self.protocol = protocol

    def to_dict(self):
        borrow = {}
        for key, value in self.__dict__.items():
            borrow[key] = value
        return borrow
