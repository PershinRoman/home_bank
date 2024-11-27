import pytest

from src.get_date import get_date_


def test_valid_date():
    '''Функция корректно преобразует даты'''
    assert get_date_('2024-03-11') == '11.03.2024'
    assert get_date_('1999-12-31') == '31.12.1999'


def test_invalid_date_format():
    '''Вызывает исключение, при передачи в неправильном формате'''
    with pytest.raises(ValueError):
        get_date_('03/11/2024')
    with pytest.raises(ValueError):
        get_date_('2024-02-30')


def test_edge_cases():
    '''високосные годый'''
    assert get_date_('2024-02-29') == '29.02.2024'
