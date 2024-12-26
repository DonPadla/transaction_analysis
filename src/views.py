import json
from pathlib import Path

from src.utils import (get_currency_rates, get_greeting, get_open_file, get_show_card_info, get_show_SP500,
                       get_top_transactions_by_amount)

imported_file = Path(__file__).resolve().parent.parent / 'data' / 'operations.xlsx'
currency_list = ["USD", "EUR"]
ticker_list = ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]
date = '2020-12-20 12:12:12'


def get_main_page(date):
    """ Реализует логику функций собранных в модуле utils. """

    result = json.dumps({
        "greeting": get_greeting(),
        "cards": get_show_card_info(get_open_file(imported_file, date)),
        "top_transactions": get_top_transactions_by_amount(get_open_file(imported_file, date)),
        "currency_rates": get_currency_rates(currency_list),
        "stock_prices": get_show_SP500(ticker_list)
    })
    return result
