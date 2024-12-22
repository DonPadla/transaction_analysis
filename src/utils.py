# Вспомогательные функции, необходимые для работы функции страницы «Главная», расположены в модуле utils.py
# Вспомогательные функции, необходимые для работы функции страницы «Главная», используют библиотеку json
# Вспомогательные функции, необходимые для работы функции страницы «Главная», используют API.
# Вспомогательные функции, необходимые для работы функции страницы «Главная», используют библиотеку datetime
# Вспомогательные функции, необходимые для работы функции страницы «Главная», используют библиотеку logging
# Вспомогательные функции, необходимые для работы функции страницы «Главная», используют библиотеку pandas
import os

import pandas as pd
import logging
from datetime import datetime
import datetime
import requests
from dotenv import load_dotenv
import json


def get_open_file(imported_file: str, date=None):
    """ Принимает путь до xlsx файла, открывает его и фильтрует по дате. """

    logging.info('Открытие xlsx файла')
    reader = pd.read_excel(imported_file)
    reader['Дата операции'] = pd.to_datetime(reader['Дата операции'], format='%d.%m.%Y %H:%M:%S')
    end_date = datetime.datetime.strptime(date, "%d.%m.%Y %H:%M:%S")
    start_date = end_date.replace(day=1, hour=00, minute=00, second=00)
    filtered_data = reader[(reader['Дата операции'] >= start_date) & (reader['Дата операции'] <= end_date)]
    return filtered_data


def get_greeting():
    " Приветствует пользователя исходя из времени суток "

    logging.info('Вычесление времени. Подбор приветствия.')
    datetime_now = datetime.datetime.now()
    hour_now = int(datetime_now.strftime("%H"))
    greeting = ''

    if 0 <= hour_now < 6:
        greeting = 'Доброй ночи.'

    elif 6 <= hour_now < 12:
        greeting = 'Доброе утро.'

    elif 12 <= hour_now < 18:
        greeting = 'Добрый день.'

    else:
        greeting = 'Добрый вечер.'

    return greeting


def get_show_card_info(imported_file):
    """ Выводит информацию по каждой карте (маску, общую сумму расходов, кешбек) """

    card_info_dict = {}
    logging.info('Получение информации по картам за указанный период')

    for index, row in imported_file.iterrows():

        if type(row['Номер карты']) is str:

            card_number = row['Номер карты'][-4:]
            expenses = row['Сумма операции'] if pd.notnull(row['Сумма операции']) else 0
            cashback = row['Кэшбэк'] if pd.notnull(row['Кэшбэк']) else 0

            if card_number not in card_info_dict:
                card_info_dict[card_number] = {"last_digits": card_number, "total_spent": expenses,
                                               "cashback": cashback}

            else:
                card_info_dict[card_number]['total_spent'] += expenses
                card_info_dict[card_number]['cashback'] += cashback

    card_info = [card_info_dict[key] for key in card_info_dict]
    return card_info


def get_top_transactions_by_amount(imported_file):
    """ Выводит информацию по пяти топ транзакциям по сумме """

    sorted_by_price = imported_file.sort_values(by='Сумма платежа').head()
    operation_info = []

    for index, row in sorted_by_price.iterrows():
        date = row['Дата платежа']
        amount = row['Сумма операции']
        category = row['Категория']
        description = row['Описание']

        operation_info.append({
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        })

    return operation_info


def get_currency_rates(first_currency='USD', second_currency='EUR'):
    """ Выводит курс валют. """

    currency_info = []

    load_dotenv()
    api_key = os.getenv("API_KEY")
    headers = {"apikey": api_key}
    payload = {}
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={first_currency}&amount=1"
    response = requests.request("GET", url, headers=headers, data=payload)
    result = json.loads(response.text)

    currency_info.append({'currency': result['query']['from'],
                          'rate': result['info']['rate']})

    load_dotenv()
    api_key = os.getenv("API_KEY")
    headers = {"apikey": api_key}
    payload = {}
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={second_currency}&amount=1"
    response = requests.request("GET", url, headers=headers, data=payload)
    result = json.loads(response.text)

    currency_info.append({'currency': result['query']['from'],
                          'rate': result['info']['rate']})

    return currency_info


def get_show_SP500(ticker_list):
    " Выводит информацию об акциях S&P500. "

    load_dotenv()
    api_key = os.getenv("API_KEY_POLYGON")
    headers = {"apikey": api_key}
    list_stocks = []

    for ticker in ticker_list:

        date_yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
        three_days_ago = datetime.datetime.now() - datetime.timedelta(days=3)
        stop_date = date_yesterday.strftime("%Y-%m-%d")
        start_date = three_days_ago.strftime("%Y-%m-%d")
        url = f'https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{start_date}/{stop_date}?apiKey={api_key}'
        response = requests.request("GET", url, headers=headers)

        if response.status_code == 200:
            result = response.json()

            if result['resultsCount'] > 0:
                closing_price = result['results'][0]['c']
                list_stocks.append({"stock": ticker, "price": closing_price})

    return list_stocks
