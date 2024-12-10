from datetime import datetime


def get_date_(date: str) -> str:
    """
    Преобразуем строку с датой из формата '2024-03-11'
    в формат 'ДД.ММ.ГГГГ'

    :param date: Дата в формате ISO 'YYYY-MM-DD'
    :return: Дата в формате 'ДД.ММ.ГГГГ'
    """
    date_list: datetime = datetime.fromisoformat(date)  # Дата из входной строки

    return date_list.strftime('%d.%m.%Y')  # Форматирование даты


print(get_date_('2024-03-11'))
