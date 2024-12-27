class Tools:
    def __init__(self):
        pass

    def get_implied_odds(self, odds):
        if odds < 0:
            return abs(odds) / (abs(odds) + 100)
        return 100 / (odds + 100)
    
    def is_arbitrage_opportunity(self, odds1, odds2):
        return self.get_implied_odds(odds1) + self.get_implied_odds(odds2) < 1
           