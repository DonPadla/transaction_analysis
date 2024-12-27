import datetime
import json
from unittest.mock import Mock, patch

import pandas as pd

from src.utils import (get_currency_rates, get_greeting, get_open_file, get_show_card_info, get_show_sp500,
                       get_top_transactions_by_amount)


def test_get_open_file():
    """ Тест передачи пустой строки или int """
    assert get_open_file("") == "Файл не найден"
    assert get_open_file(123) == "Передано невалидное значение"


@patch("datetime.datetime")
def test_get_greeting(mock):
    """ Тест работы функции, если сейчас 2 часа ночи """
    mock.now.return_value = datetime.datetime(2)
    assert get_greeting() == "Доброй ночи."


def test_get_show_card_info(data_for_test, result_show_card_info):
    """ Тестирование вывода информации по картам """
    df = pd.DataFrame(data_for_test)
    assert get_show_card_info(df) == result_show_card_info


def test_card_info_none():
    """ Тест передачи пустой строки или не передачи вовсе """
    assert get_show_card_info("что-то") == "Передано невалидное значение"
    assert get_show_card_info(None) == "Передано невалидное значение"


def test_top_transactions(data_for_test, result_top_transactions):
    """ Тест вывода информации по топ транзакциям """
    df = pd.DataFrame(data_for_test)
    assert get_top_transactions_by_amount(df) == result_top_transactions


@patch('requests.request')
def test_currency_rates(mock):
    """ Тест конвертации валют """
    mock_response_data = {'query': {'from': 'USD'}, 'info': {'rate': 36.0}}
    mock.return_value = Mock(status_code=200, text=json.dumps(mock_response_data))
    result = get_currency_rates(["USD"])
    assert result[0]['currency'] == 'USD'
    assert result[0]['rate'] == 36.0


@patch("requests.request")
def test_show_sp500(mock):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'resultsCount': 1, 'results': [{'c': "довольно дорого"}]}
    mock.return_value = mock_response
    result_func = get_show_sp500(["акция, которой у меня нет"])
    expected_result = [{"stock": "акция, которой у меня нет", "price": "довольно дорого"}]
    assert result_func == expected_result
