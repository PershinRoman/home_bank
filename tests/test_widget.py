from src.widget import get_mask_account, get_mask_card_number, mask_account_card

def test_get_mask_account(account_number):
    assert ("7000792289606361") == "7000792289606361"

def test_get_mask_card_number(card_number):
    assert ('6543 8765 9077 6457') == '6543 8765 9077 6457'

def test_mask_account_card(name_card):
    assert ('Visa Platinum 7000792289606361') == 'Visa Platinum 700079228960636'
