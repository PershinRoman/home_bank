import pytest

from src.processing import filter_by_state, sort_by_date

@pytest.mark.parametrize(
    'correct_date',
    [
        ({'id': 939719570, 'state': 'EXECUTED', 'date': '425572'}),
        ({'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30'}),
        ({'id': 939719570, 'state': 'EXECUTED', 'date': ''})
    ]
)
def test_sort_by_date_wrong_date(correct_date):
    with pytest.raises(Exception):
        sort_by_date(correct_date)
