import pytest


@pytest.fixture
def number_card():
    return 'Visa Platinum 7000792289606361'


def test_get_mask_card_number(number_card):
    number_card = (
            number_card[:4] + " " +
            number_card[4:6] + "** ****" +
            number_card[-4:]
    )
    assert number_card


def test_get_mask_account(number_card):
    number_card = str(number_card)
    number_card = "**" + number_card[-4:]
    masked_account = "**" + number_card[-4:]
    assert masked_account


def test_mask_account_card(number_card):
    '''Функция обрабатывает строки для карт и счетов
    Вызывает ошибку для некорректной длин'''
    assert mask_account_card('Счет 12345678') == 'Счет **5678'
    assert mask_account_card(number_card) == 'Visa Platinum **6361'

    with pytest.raises(ValueError):
        mask_account_card('Счет 123')
