class stock:
    def __init__(self, date, close, open, high, low, volume):
        self.date = date
        self.close = float(close)
        self.open = float(open)
        self.high = float(high)    
        self.low = float(low)
        self.volume = int(volume)