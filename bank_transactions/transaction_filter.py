import re
from typing import List, Dict


def filter_transactions_by_description(transactions: List[Dict], search_string: str) -> List[Dict]:
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction.get('description', ''))]


def count_operations_by_category(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    category_count = {category: 0 for category in categories}
    for transaction in transactions:
        description = transaction.get('description', '')
        for category in categories:
            if category.lower() in description.lower():
                category_count[category] += 1
    return category_count
