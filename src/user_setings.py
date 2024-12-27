import json
from pathlib import Path
from typing import Any, Dict


def load_user_settings(imported_file_path: str) -> Dict[str, Any]:
    """ Выводит пользовательские настройки из json файла """

    try:
        with open(imported_file_path, 'r', encoding='utf-8') as f:
            settings = json.load(f)
            return settings

    except FileNotFoundError:
        print(f"Файл настроек {imported_file_path} не найден.")
        return {}

    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON в файле {imported_file_path}.")
        return {}


file_path = Path(__file__).resolve().parent.parent / 'user_settings.json'
user_settings = load_user_settings(file_path)
default_imported_file = Path(__file__).resolve().parent.parent / 'data' / 'operations.xlsx'
currency_list = user_settings.get("default_imported_file", [])
ticker_list = user_settings.get("ticker_list", [])
date = user_settings.get("date", [])
