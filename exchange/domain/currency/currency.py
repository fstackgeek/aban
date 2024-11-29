class Currency:
    def __init__(self, code, price):
        self.code = code
        self.price = price

    def get_dollar_value(self, amount):
        return self.price * amount
