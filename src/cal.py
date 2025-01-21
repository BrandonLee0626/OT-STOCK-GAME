from team import Team
from stock import Stock
from file import read_previous_results

class RoundProcess:
    def __init__(self, round_data, round_number):
        self.round_data = round_data
        if round_number == 1:
            Stock.load_initial_prices() 
        else:
            Stock.update_prices(round_number)  
        self.teams = self.initialize_teams(round_number)
        self.stocks = Stock.get_stock_list()
        self.round_number = round_number

    def initialize_teams(self, round_number):
        teams = {}
        if round_number > 1:
            previous_results = read_previous_results(f'../results/result{round_number - 1}.txt')
            for result in previous_results:
                team_name = result['team']
                if team_name not in teams:
                    teams[team_name] = Team(team_name)
                teams[team_name].load_from_summary(result)
        for data in self.round_data:
            team_name = data['team']
            if team_name not in teams:
                teams[team_name] = Team(team_name)
        return teams

    def process_round(self):
        for data in self.round_data:
            team = self.teams[data['team']]
            stock_name = data['stock'].upper()  
            action = data['action']
            quantity = int(data['quantity'])
            if action == 'buy':
                team.buy_stock(stock_name, quantity, self.stocks[stock_name])
            elif action == 'sell':
                team.sell_stock(stock_name, quantity, self.stocks[stock_name])
        
        if self.round_number == 1:
            Stock.update_prices(1)
            self.stocks = Stock.get_stock_list()

        return [team.get_summary() for team in self.teams.values()]