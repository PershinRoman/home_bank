import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    ''' Маскирование карты
    Работа с целыми числами
    Ошибка при не верном вводе'''

    assert get_mask_card_number('1234567812345678') == '1234 56** ****5678'
    assert get_mask_card_number(9876543210123456) == '9876 54** ****3456'

    with pytest.raises(ValueError):
        get_mask_card_number('12345')
    with pytest.raises(ValueError):
        get_mask_card_number('123456789001234567889')


def test_get_mask_account():
    '''Проверка на маскировку
    Работа с целыми числами
    Ошибка на короткий ввод'''
    assert get_mask_account('12345678') == '**5678'
    assert get_mask_account('9821472146') == '**2146'
    assert get_mask_account('1234') == '**1234'

    with pytest.raises(ValueError):
        get_mask_account('123')
    with pytest.raises(ValueError):
        get_mask_account('12')


if __name__ == '__main__':
    pytest.main()
