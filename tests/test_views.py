from src.views import get_main_page


def test_get_main_page():
    assert get_main_page('что-то') == "Введите дату и время в формате YYYY-MM-DD HH:MM:SS"
    assert get_main_page('') == "Введите дату и время в формате YYYY-MM-DD HH:MM:SS"
