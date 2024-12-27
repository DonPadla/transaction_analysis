import pytest


@pytest.fixture
def data_for_test():
    return {
        'Номер карты': ['*3456', '*0001', '*4444', '*3456'],
        'Сумма операции': [100, 200, 300, 150],
        'Кэшбэк': [5, 10, 15, 7],
        'Дата платежа': ['2021-12-12', '2021-12-13', '2021-12-14', '2021-12-15'],
        'Сумма платежа': [100, 200, 300, 150],
        'Категория': ['Еда', 'Транспорт', 'Развлечения', 'Покупки'],
        'Описание': ['Ресторан', 'Такси', 'Кино', 'Магазин']
    }


@pytest.fixture
def result_show_card_info():
    return [
        {'last_digits': '3456', 'total_spent': 250, 'cashback': 12},
        {'last_digits': '0001', 'total_spent': 200, 'cashback': 10},
        {'last_digits': '4444', 'total_spent': 300, 'cashback': 15}
    ]


@pytest.fixture
def result_top_transactions():
    return [
        {'date': '2021-12-12', 'amount': 100, 'category': 'Еда', 'description': 'Ресторан'},
        {'date': '2021-12-15', 'amount': 150, 'category': 'Покупки', 'description': 'Магазин'},
        {'date': '2021-12-13', 'amount': 200, 'category': 'Транспорт', 'description': 'Такси'},
        {'date': '2021-12-14', 'amount': 300, 'category': 'Развлечения', 'description': 'Кино'},
    ]
