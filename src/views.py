# Функция для страницы «Главная» расположена в модуле  views.py
# Функция для страницы «Главная» отдает корректный JSON-ответ согласно ТЗ.

import datetime


# Шаблон получения даты и приветствия
now_datetime = datetime.datetime.now()
date_str = int(now_datetime.strftime("%H"))
date_range = None

if 0 <= date_str <= 5:
    print('Good night')

elif 6 <= date_str <= 11:
    print('Good morning')

elif 12 <= date_str <= 17:
    print('Good day')

else:
    print('Good evening')
