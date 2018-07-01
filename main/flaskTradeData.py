from flask import Flask
import json
from flask_cors import CORS
from yahoofinancials import YahooFinancials
from stock_data_utilities.stock_data_extractor import StockDataExtractor

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/balance_sheet/<comp_code>', methods=['GET'])
def balance_sheet_provider(comp_code):
    yahoo_financials = YahooFinancials(comp_code)
    #balance_sheet_raw = json.dumps(yahoo_financials.get_financial_stmts('annual', 'balance'))
    #income_statement_raw = json.dumps(yahoo_financials.get_financial_stmts('annual', 'income'))
    earnings_per_share = yahoo_financials.get_earnings_per_share()
    pe_rat = yahoo_financials.get_pe_ratio()
    print(earnings_per_share)

    balance_sheet_raw = {"balanceSheetHistory": {"KO":
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
    income_statement_raw = {"incomeStatementHistory": {"KO":
            [{"2017-12-31": {"researchDevelopment": None,
                             "effectOfAccountingCharges": None,
                             "incomeBeforeTax": 6742000000,
                             "minorityInterest": 1905000000,
                             "netIncome": 1248000000,
                             "sellingGeneralAdministrative": 14653000000,
                             "grossProfit": 22154000000,
                             "ebit": 7583000000,
                             "operatingIncome": 7501000000,
                             "otherOperatingExpenses": None,
                             "interestExpense": 841000000,
                             "extraordinaryItems": None,
                             "nonRecurring": None,
                             "otherItems": None,
                             "incomeTaxExpense": 5560000000,
                             "totalRevenue": 35410000000,
                             "totalOperatingExpenses": 0,
                             "costOfRevenue": 13256000000,
                             "totalOtherIncomeExpenseNet": -989000000,
                             "discontinuedOperations": 101000000,
                             "netIncomeFromContinuingOps": 1182000000,
                             "netIncomeApplicableToCommonShares": 1248000000}},
             {"2016-12-31": {"researchDevelopment": None,
                             "effectOfAccountingCharges": None,
                             "incomeBeforeTax": 8136000000,
                             "minorityInterest": 158000000,
                             "netIncome": 6527000000,
                             "sellingGeneralAdministrative": 16772000000,
                             "grossProfit": 25398000000,
                             "ebit": 8869000000,
                             "operatingIncome": 8626000000,
                             "otherOperatingExpenses": None,
                             "interestExpense": 733000000,
                             "extraordinaryItems": None,
                             "nonRecurring": None,
                             "otherItems": None,
                             "incomeTaxExpense": 1586000000,
                             "totalRevenue": 41863000000,
                             "totalOperatingExpenses": 0,
                             "costOfRevenue": 16465000000,
                             "totalOtherIncomeExpenseNet": -592000000,
                             "discontinuedOperations": 101000000,
                             "netIncomeFromContinuingOps": 6550000000,
                             "netIncomeApplicableToCommonShares": 6527000000}},
             {"2015-12-31": {"researchDevelopment": None,
                             "effectOfAccountingCharges": None,
                             "incomeBeforeTax": 9605000000,
                             "minorityInterest": 210000000,
                             "netIncome": 7351000000,
                             "sellingGeneralAdministrative": 18084000000,
                             "grossProfit": 26812000000,
                             "ebit": 10461000000,
                             "operatingIncome": 8728000000,
                             "otherOperatingExpenses": None,
                             "interestExpense": 856000000,
                             "extraordinaryItems": None,
                             "nonRecurring": None,
                             "otherItems": None,
                             "incomeTaxExpense": 2239000000,
                             "totalRevenue": 44294000000,
                             "totalOperatingExpenses": 0,
                             "costOfRevenue": 17482000000,
                             "totalOtherIncomeExpenseNet": 1244000000,
                             "discontinuedOperations": 101000000,
                             "netIncomeFromContinuingOps": 7366000000,
                             "netIncomeApplicableToCommonShares": 7351000000}}]}}

    balance_sheet = balance_sheet_raw["balanceSheetHistory"]['KO']
    income_statement = income_statement_raw["incomeStatementHistory"]['KO']
    EPS = 0.33

    company_data_provider_object = StockDataExtractor('KO','COKE', balance_sheet, income_statement, EPS, pe_rat)

    print(company_data_provider_object.balance_sheet_data)
    print(company_data_provider_object.income_statement_data)

    print(company_data_provider_object.return_data_for_stock())
    output_dict = {'EPS': 1, 'Net Income': 1}

    s = json.dumps(company_data_provider_object.return_data_for_stock())

    return s

if __name__ == '__main__':
    app.run()

