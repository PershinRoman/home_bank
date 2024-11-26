import pytest

from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize(
    'number_user, masked',
    [
        ('12345123451234512345', '**2345'),
        ('45678456784567845678', '**5678'),
        ('12389123891238912389', '**2389'),
    ],
)
def test_get_mask_number(number_user, masked):
    assert get_mask_account(number_user) == masked


@pytest.mark.parametrize(
    'number_card, masked',
    [
        ('1234512345123451', '1234 51** ****3451'),
        ('4567845678456784', '4567 84** ****6784'),
        ('1238912389123891', '1238 91** ****3891'),
    ],
)
def test_get_mask_numbers(number_card, masked):
    assert get_mask_card_number(number_card) == masked