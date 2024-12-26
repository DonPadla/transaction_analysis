import datetime
from typing import Optional

import pandas as pd
from dateutil.relativedelta import relativedelta
from pandas import DataFrame

from src.logging_settings import logger


def get_report(file_name='repo_for_spending'):
    """ Декоратор записывает результат декорируемой функции в файл"""

    def decorator(func):
        def wraper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result is DataFrame:
                result_str = result.to_json()
            else:
                result_str = str(result)
            with open(file_name, "a", encoding="utf-8") as f:
                f.write(result_str)
            return result

        return wraper

    return decorator


@get_report()
def spending_by_category(imported_file: str, category: str, date: Optional[str] = None) -> DataFrame | str:
    """ Принимает путь к файлу, категорию, и дату.
    Возвращает траты по заданной категории за последние три месяца. """

    try:
        reader = pd.read_excel(imported_file)
        reader['Дата операции'] = pd.to_datetime(reader['Дата операции'], format="%d.%m.%Y %H:%M:%S")
        if date is not None:
            stop_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        else:
            stop_date = datetime.datetime.now()
        start_date = stop_date - relativedelta(months=3)
        filtered_data = reader[
            (reader["Дата операции"] >= start_date)
            & (reader["Дата операции"] <= stop_date)
            & (reader["Категория"] == category)
            ]
        sum_category = filtered_data["Сумма операции"].sum()

        return pd.DataFrame({category: [sum_category]})

    except ValueError:
        logger.error("Переданы невалидные значения.")

        return "Ошибка"
