from flask import Flask
import json
import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/balance_sheet/<comp_code>', methods=['GET'])
def balance_sheet_provider(comp_code):
    # yahoo_financials = YahooFinancials(comp_code)
    # result1 = json.dumps(yahoo_financials.get_financial_stmts('annual', 'balance'))
    result1 = {"balanceSheetHistory": {"KO":
             [{"2017-12-31": {"intangibleAssets": 7235000000,
                              "capitalSurplus": 15864000000,
                              "totalLiab": 68919000000,
                              "totalStockholderEquity": 17072000000,
                              "minorityInterest": 1905000000,
                              "otherCurrentLiab": 2169000000,
                              "totalAssets": 87896000000,
                              "commonStock": 1760000000,
                              "otherCurrentAssets": 7993000000,
                              "retainedEarnings": 60430000000,
                              "otherLiab": 10504000000,
                              "goodWill": 9401000000,
                              "treasuryStock": -60982000000,
                              "otherAssets": 3231000000,
                              "cash": 6006000000,
                              "totalCurrentLiabilities": 27194000000,
                              "deferredLongTermAssetCharges": 331000000,
                              "shortLongTermDebt": 47754000000,
                              "otherStockholderEquity": -10305000000,
                              "propertyPlantEquipment": 8203000000,
                              "totalCurrentAssets": 36545000000,
                              "longTermInvestments": 23281000000,
                              "netTangibleAssets": 436000000,
                              "shortTermInvestments": 14669000000,
                              "netReceivables": 3667000000,
                              "longTermDebt": 31221000000,
                              "inventory": 2655000000,
                              "accountsPayable": 2288000000}},
              {"2016-12-31": {"intangibleAssets": 10499000000,
                              "capitalSurplus": 14993000000,
                              "totalLiab": 64050000000,
                              "totalStockholderEquity": 23062000000,
                              "minorityInterest": 158000000,
                              "otherCurrentLiab": 1936000000,
                              "totalAssets": 87270000000,
                              "commonStock": 1760000000,
                              "otherCurrentAssets": 3592000000,
                              "retainedEarnings": 65502000000,
                              "otherLiab": 7786000000,
                              "goodWill": 10629000000,
                              "treasuryStock": -59193000000,
                              "otherAssets": 2928000000,
                              "cash": 8555000000,
                              "totalCurrentLiabilities": 26532000000,
                              "deferredLongTermAssetCharges": 326000000,
                              "shortLongTermDebt": 45801000000,
                              "otherStockholderEquity": -11205000000,
                              "propertyPlantEquipment": 10635000000,
                              "totalCurrentAssets": 34010000000,
                              "longTermInvestments": 18569000000,
                              "netTangibleAssets": 1934000000,
                              "shortTermInvestments": 13646000000,
                              "netReceivables": 3856000000,
                              "longTermDebt": 29732000000,
                              "inventory": 2675000000,
                              "accountsPayable": 2682000000}},
              {"2015-12-31": {"intangibleAssets": 12843000000,
                              "capitalSurplus": 14016000000,
                              "totalLiab": 64232000000,
                              "totalStockholderEquity": 25554000000,
                              "minorityInterest": 210000000,
                              "otherCurrentLiab": 2333000000,
                              "totalAssets": 89996000000,
                              "commonStock": 1760000000,
                              "otherCurrentAssets": 4748000000,
                              "retainedEarnings": 65018000000,
                              "otherLiab": 8760000000,
                              "goodWill": 11289000000,
                              "treasuryStock": -55240000000,
                              "otherAssets": 3030000000,
                              "cash": 7309000000,
                              "totalCurrentLiabilities": 26929000000,
                              "deferredLongTermAssetCharges": 360000000,
                              "shortLongTermDebt": 44401000000,
                              "otherStockholderEquity": -10174000000,
                              "propertyPlantEquipment": 12571000000,
                              "totalCurrentAssets": 33395000000,
                              "longTermInvestments": 16868000000,
                              "netTangibleAssets": 1422000000,
                              "shortTermInvestments": 12591000000,
                              "netReceivables": 4466000000,
                              "longTermDebt": 19100000000,
                              "inventory": 3100000000,
                              "accountsPayable": 2089000000}}]}}
    inner_dict = result1["balanceSheetHistory"]['KO']

    def decide_latest_year(year_list):
        return reversed(sorted(year_list, key=lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))).__next__()

    def create_year_list(local_dict):
        year_list = list()
        for dateData in local_dict:
            for key, value in dateData.items():
                year_list.append(key)
        return year_list

    def get_latest_year_data():
        latest_year = decide_latest_year(create_year_list(inner_dict))
        for year_dict in inner_dict:
            try:
                balance_sheet_object = year_dict[latest_year]
                print(balance_sheet_object)
                print(balance_sheet_object.__getitem__('intangibleAssets'))
                return balance_sheet_object
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")

    s = json.dumps(get_latest_year_data())

    return s

if __name__ == '__main__':
    app.run()

