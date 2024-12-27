import json

from src.logging_settings import logger
from src.user_setings import currency_list, date, default_imported_file, ticker_list
from src.utils import (get_currency_rates, get_greeting, get_open_file, get_show_card_info, get_show_sp500,
                       get_top_transactions_by_amount)


def get_main_page(imported_file=default_imported_file, input_date=date):
    """ Реализует логику функций собранных в модуле utils. """

    try:
        result = json.dumps({
            "greeting": get_greeting(),
            "cards": get_show_card_info(get_open_file(imported_file, input_date)),
            "top_transactions": get_top_transactions_by_amount(get_open_file(imported_file, input_date)),
            "currency_rates": get_currency_rates(currency_list),
            "stock_prices": get_show_sp500(ticker_list)
        }, ensure_ascii=False)
        return result

    except AttributeError:
        logger.error("Передано невалидное значение.")
        return "Введите дату и время в формате YYYY-MM-DD HH:MM:SS"
