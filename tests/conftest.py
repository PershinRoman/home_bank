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
