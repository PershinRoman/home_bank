import pytest

from src.widget import get_mask_account, get_mask_card_number, mask_account_card

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


@pytest.mark.parametrize('condition, expected_result', [
    ('1234567812345678', '1234 56** ****5678'),
    (1234567812345678, '1234 56** ****5678')
])
def test_mask_card_number(condition, expected_result):
    '''Правильная маскировка карты
    Ошибка для коротких номеров карты'''
    assert get_mask_card_number(condition) == expected_result


def test_mask_account_card():
    '''Функция обрабатывает строки для карт и счетов
    Вызывает ошибку для некорректной длин'''
    assert mask_account_card('Счет 12345678') == 'Счет **5678'
    assert mask_account_card('Карта 1234567812345678') == 'Карта **5678'

    with pytest.raises(ValueError):
        mask_account_card('Счет 123')
