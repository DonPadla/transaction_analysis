import json

import pandas as pd

from src.logging_settings import logger


def get_profitable_categories(imported_file: str, year: int, month: int) -> str:
    """ Принимает путь к файлу, месяц и год, фильтрует по указанным месяцу и году.
    Возвращает json строку с тремя топ категориями и суммой кэшбэка, отсортированными по убыванию. """

    try:
        reader = pd.read_excel(imported_file)
        reader['Дата операции'] = (pd.to_datetime(
                reader['Дата операции'], format='%d.%m.%Y %H:%M:%S'
            )
        )
        filtered_data = reader[
            (reader["Дата операции"].dt.month == month) &
            (reader["Дата операции"].dt.year == year) &
            (reader["Кэшбэк"].notnull())
            ]
        categories_group = filtered_data.groupby("Категория")["Кэшбэк"].sum().reset_index()
        sorted_categories = categories_group.sort_values(by="Кэшбэк", ascending=False).head(3)

        df_to_dict = sorted_categories.set_index("Категория")["Кэшбэк"].to_dict()

        result = json.dumps(df_to_dict, ensure_ascii=False)
        return result

    except Exception as e:
        logger.error(f"Ошибка: {e}")
        return json.dumps({"error": str(e)})
