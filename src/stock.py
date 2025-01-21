class Stock:
    stocks = {}

    def __init__(self, name, initial_price):
        self.name = name
        self.price = initial_price

    def update_price(self, new_price):
        self.price = new_price

    def get_price(self):
        return self.price

    def __str__(self):
        return f"Stock(name={self.name}, price={self.price})"

    @classmethod
    def load_initial_prices(cls):
        filepath = '../stock/stock0.txt'
        with open(filepath, 'r') as file:
            for line in file:
                name, price = line.strip().split(', ')
                cls.stocks[name.upper()] = int(price)

    @classmethod
    def update_prices(cls, round_number):
        filepath = f'../stock/stock{round_number}.txt'
        with open(filepath, 'r') as file:
            for line in file:
                name, price = line.strip().split(', ')
                cls.stocks[name.upper()] = int(price)

    @classmethod
    def get_stock_list(cls):
        return cls.stocks