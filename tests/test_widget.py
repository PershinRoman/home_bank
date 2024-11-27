import pytest

from src.widget import mask_account_card, get_mask_account, get_mask_card_number

if __name__ == '__main__':
    pytest.main()


def test_get_mask_account():
    '''Проверка правильности маскировки счетов
    ошибка для коротких номеров'''
    assert get_mask_account('12345678') == '**5678'
    assert get_mask_account('12983659') == '**3659'
    assert get_mask_account(1234) == '**1234'

    with pytest.raises(ValueError):
        get_mask_account('123')
    with pytest.raises(ValueError):
        get_mask_account('1')


def test_mask_card_number():
    '''Правильная маскировка карты
    Ошибка для коротких номеров карты'''
    assert get_mask_card_number('1234567812345678') == '1234 56** ****5678'
    assert get_mask_card_number(1234567812345678) == '1234 56** ****5678'

    with pytest.raises(ValueError):
        get_mask_card_number('12345')
    with pytest.raises(ValueError):
        get_mask_card_number('12182639861239816129863126893')


def test_mask_account_card():
    '''Функция обрабатывает строки для карт и счетов
    Вызывает ошибку для некорректной длин'''
    assert mask_account_card('Счет 12345678') == 'Счет **5678'
    assert mask_account_card('Карта 1234567812345678') == 'Карта **5678'

    with pytest.raises(ValueError):
        mask_account_card('Счет 123')
