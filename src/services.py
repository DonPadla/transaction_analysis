import json

import pandas as pd


def get_profitable_categories(imported_file, year, month):
    """ Принимает путь до xlsx файла, месяц и год. Открывает файл, фильтрует по указанным месяцу и году.
    Возвращает json строку с тремя топ категориями и суммой кэшбэка, отсортированными по убыванию. """

    reader = pd.read_excel(imported_file)
    reader['Дата операции'] = pd.to_datetime(reader['Дата операции'], format='%d.%m.%Y %H:%M:%S')
    filtered_data = reader[
        (reader['Дата операции'].dt.month == month)
        & (reader['Дата операции'].dt.year == year)
        & (reader['Кэшбэк'].notnull())]
    categories_group = filtered_data.groupby("Категория")["Кэшбэк"].sum().reset_index()
    sorted_categories = categories_group.sort_values(by="Кэшбэк", ascending=False).head(3)
    df_to_dict = {}

    for row, index in sorted_categories.iterrows():
        df_to_dict[index["Категория"]] = index["Кэшбэк"]

    result = json.dumps(df_to_dict, ensure_ascii=False)

    return result
