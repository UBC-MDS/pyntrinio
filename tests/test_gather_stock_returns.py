from pyntrinio.pyntrinio import gather_stock_returns

# helper data
api_key = 'OjhlMjhjNTBmY2IyMWJiMWE0MTExYjQwNWZmZTVkZWM1'
ticker = ['AAPL', 'CSCO']
buy_date = '2011-01-01' 
sell_date = '2019-12-10' 
rtn_appl = 555.38
rtn_csco = 176.01

def test_return_accuracy():
    """
    Test if the function correctly calculates the returns.
    """
    result = gather_stock_returns(api_key, ['AAPL', 'CSCO'], buy_date, sell_date)
    assert result["Return (%)"][0] == rtn_appl
    assert result["Return (%)"][1] == rtn_csco
    assert result.shape == (2, 6)


def api_key_test():
    """
    Give a wrong api_key, see if the function correctly handles the exception.
    """
    msg = "Incorrect API Key - please input a valid API key as a string"
    assert gather_stock_returns('abc', 'AAPL', buy_date, sell_date) == msg
    
def date_format_test():
    """
    See if the function correctly handles the input dates in wrong formats.
    """
    msg = "Invalid Date format - please input the date as a string with format %Y-%m-%d"
    assert gather_stock_returns(api_key, 'AAPL', '2018', sell_date) == msg


def date_logic_test():
    """
    Make sell_date earlier to buy date. See if the function handles this exception.
    """
    msg = "Invalid Input: `sell_date` is earlier than `buy_date`."
    assert gather_stock_returns(api_key, 'AAPL', buy_date='2019-01-01', sell_date='2017-01-01') == msg
