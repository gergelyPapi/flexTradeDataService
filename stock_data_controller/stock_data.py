class StockDataProvider:

    def __init__(self, stock_code, comp_name):
        self.stock_code = stock_code
        self.comp_name = comp_name
        self.workingCapitalRatio = 1.40
        self.earningsPerShare = 1.40
        self.priceEarningsRatio = 1.40
        self.debtEquityRatio = 1.40
        self.returnOnEquity = 1.40

    def print_info(self):
        print(self.__dict__)

