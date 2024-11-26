import pytest

from src.widget import get_mask_account, get_mask_card_number, mask_account_card

@pytest.mark.parametrize(
    'string, result',
    [
    ("Visa Platinum 7000792289606361", "Visa Platinum **6361"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("Maestro 1596837868705199", "Maestro **5199"),
    ("Счет 64686473678894779589", "Счет **9589"),
],
)
def test_mask_account_card(string, result):
    assert mask_account_card(string) == result
