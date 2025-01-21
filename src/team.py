from stock import Stock

class Team:
    def __init__(self, name):
        self.name = name
        self.portfolio = {}
        self.cash = 15000

    def buy_stock(self, stock_name, quantity, price):
        if stock_name not in self.portfolio:
            self.portfolio[stock_name] = {'quantity': 0, 'total_spent': 0}
        self.portfolio[stock_name]['quantity'] += quantity
        self.portfolio[stock_name]['total_spent'] += quantity * price
        self.cash -= quantity * price

    def sell_stock(self, stock_name, quantity, price):
        if stock_name in self.portfolio and self.portfolio[stock_name]['quantity'] >= quantity:
            self.portfolio[stock_name]['quantity'] -= quantity
            self.cash += quantity * price

    def load_from_summary(self, summary):
        stock_name = summary['stock']
        quantity = summary['quantity']
        total_spent = summary['purchase_price'] * quantity
        self.portfolio[stock_name] = {'quantity': quantity, 'total_spent': total_spent}
        self.cash = summary['current_value'] - total_spent + self.cash

    def get_summary(self):
        summary = []
        for stock_name, data in self.portfolio.items():
            quantity = data['quantity']
            total_spent = data['total_spent']
            current_value = quantity * Stock.stocks[stock_name]
            profit_loss = current_value - total_spent
            profit_loss_percentage = (profit_loss / total_spent) * 100 if total_spent != 0 else 0
            summary.append({
                'team': self.name,
                'stock': stock_name,
                'quantity': quantity,
                'purchase_price': total_spent / quantity if quantity != 0 else 0,
                'current_value': current_value,
                'profit_loss': profit_loss,
                'profit_loss_percentage': profit_loss_percentage,
                'cash': self.cash 
            })
        return summary