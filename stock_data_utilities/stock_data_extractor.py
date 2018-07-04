import datetime


class StockDataExtractor:

    def __init__(self, stock_code, comp_name, balance_sheet_data, income_statement_data, EPS, PERatio):
        self.stock_code = stock_code
        self.comp_name = comp_name
        self.balance_sheet_data = self.get_latest_statistic_data(balance_sheet_data)
        self.income_statement_data = self.get_latest_statistic_data(income_statement_data)
        self.total_liabilities = self.balance_sheet_data['totalLiab']
        self.shareholders_equity = self.balance_sheet_data['totalAssets'] - self.total_liabilities
        self.earningsPerShare = EPS
        self.priceEarningsRatio = PERatio

    def print_info(self):
        print(self.__dict__)

    @classmethod
    def decide_latest_year(cls, year_list):
        return reversed(sorted(year_list, key=lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))).__next__()

    @classmethod
    def create_year_list(cls, local_dict):
        year_list = list()
        for dateData in local_dict:
            for key, value in dateData.items():
                year_list.append(key)
        return year_list

    @classmethod
    def get_latest_statistic_data(cls, input_statistics):
        latest_year = cls.decide_latest_year(cls.create_year_list(input_statistics))
        for year_dict in input_statistics:
            try:
                statistics_object = year_dict[latest_year]
                return statistics_object
            except ValueError:
                print("Oops! That was no valid number. Try again...")

    def calculate_working_capital_ratio(self):
        return self.balance_sheet_data['totalCurrentAssets'] / self.balance_sheet_data['totalCurrentLiabilities']

    def calculate_debt_to_equity_ratio(self):
        # total assets minus its total liabilities
        return self.total_liabilities/self.shareholders_equity

    def calculate_return_on_equity(self):
        return self.income_statement_data['netIncome']/self.shareholders_equity

    @classmethod
    def round_ratio_to(cls, ratio, decimals):
        return round(ratio, decimals)

    def return_data_for_stock(self):
        stock_data = dict()
        stock_data['workingCapitalRatio'] = self.round_ratio_to(self.calculate_working_capital_ratio(), 2)
        stock_data['earningsPerShare'] = self.round_ratio_to(self.earningsPerShare, 2)
        stock_data['priceEarningsRatio'] = self.round_ratio_to(self.priceEarningsRatio, 2)
        stock_data['debtEquityRatio'] = self.round_ratio_to(self.calculate_debt_to_equity_ratio(), 2)
        stock_data['returnOnEquity'] = self.round_ratio_to(self.calculate_return_on_equity(), 2)
        return stock_data

