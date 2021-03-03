class Liquidation:

    def __init__(self, user, token_principal, token_collateral, amount_principal, amount_collateral, liquidator, timestamp, protocol):
        self.user = user
        self.token_principal = token_principal
        self.token_collateral = token_collateral
        self.amount_principal = amount_principal
        self.amount_collateral = amount_collateral
        self.liquidator = liquidator
        self.timestamp = timestamp
        self.protocol = protocol

    def to_dict(self):
        borrow = {}
        for key, value in self.__dict__.items():
            borrow[key] = value
        return borrow
