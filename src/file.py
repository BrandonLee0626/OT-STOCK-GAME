def read_round_data(filepath):
    round_data = []
    with open(filepath, 'r') as file:
        for line in file:
            team, stock, action, quantity = line.strip().split(', ')
            round_data.append({
                'team': team,
                'stock': stock,
                'action': action,
                'quantity': quantity
            })
    return round_data

def write_results(filepath, results):
    with open(filepath, 'w') as file:
        for result in results:
            for stock_summary in result:
                file.write(f"{stock_summary['team']}, {stock_summary['stock']}, {stock_summary['quantity']}, {stock_summary['purchase_price']}, {stock_summary['current_value']}, {stock_summary['profit_loss']}, {round(stock_summary['profit_loss_percentage'],2)}%\n")

def read_previous_results(filepath):
    previous_results = []
    with open(filepath, 'r') as file:
        for line in file:
            team, stock, quantity, purchase_price, current_value, profit_loss, profit_loss_percentage = line.strip().split(', ')
            previous_results.append({
                'team': team,
                'stock': stock,
                'quantity': int(quantity),
                'purchase_price': float(purchase_price),
                'current_value': float(current_value),
                'profit_loss': float(profit_loss),
                'profit_loss_percentage': float(profit_loss_percentage.strip('%'))
            })
    return previous_results