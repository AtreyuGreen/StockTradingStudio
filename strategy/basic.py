import math

class basic:
    def __init__(self, capital):
        self.capital = capital

    def run(self, number_of_stocks, current, data):
        if(current == data[0]):
            close = current.close
            number_of_stocks = math.floor(self.capital / close)
            self.capital = self.capital - math.floor(number_of_stocks * close)
        
        if(current == data[len(data)-1]):
            self.capital = number_of_stocks * current.close

        return number_of_stocks, self.capital