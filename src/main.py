from src.reports import spending_by_category
from src.services import get_profitable_categories
from src.user_setings import default_imported_file
from src.views import get_main_page


def let_show():
    choose_page = input("""Куда пойдем?
    1. Веб-страницы
    2. Сервисы
    3. Отчеты
    : """)

    while True:

        if choose_page == "1":
            print(get_main_page())
            break

        elif choose_page == "2":
            input_year = int(input("Введите год в формате YYYY: "))
            input_month = int(input("Введите месяц: "))
            print(get_profitable_categories(default_imported_file, input_year, input_month))
            break

        elif choose_page == "3":
            input_category = input("""Здесь я покажу траты за последние три месяца, по категории, которую вы напишите
            здесь: """)
            print(spending_by_category(default_imported_file, str(input_category)))
            break

        else:
            print("Не делай так!")
