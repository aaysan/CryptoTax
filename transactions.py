class Transaction(object):
    def __init__(self, description, crypto_currency, crypto_amount, date_acquired, date_sold, proceeds, currency):
        self.date_acquired = date_acquired
        self.date_sold = date_sold
        self.description = description
        self.crypto_currency = crypto_currency
        self.crypto_amount = crypto_amount
        self.proceeds = proceeds
        self.currency = currency

    def print(self):
        if self.date_sold is None:
            # print("BUY")
            print(self.description, self.crypto_currency, self.crypto_amount, self.currency, self.proceeds, self.date_acquired)
        else:
            # print("SELL")
            print(self.description, self.crypto_currency, self.crypto_amount, self.currency, self.proceeds, self.date_sold)
