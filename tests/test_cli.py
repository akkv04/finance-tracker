from models.transaction import Transaction
from cli import calculate_summary


def test_summary_calculation():
    transactions = [
        Transaction(50.0, "groceries", "2026-06-22", "weekly shop"),
        Transaction(20.0, "groceries", "2026-06-23", "snacks"),
        Transaction(12.0, "coffee", "2026-06-23", "latte"),
    ]

    totals = calculate_summary(transactions)

    assert totals == {"groceries": 70.0, "coffee": 12.0}
