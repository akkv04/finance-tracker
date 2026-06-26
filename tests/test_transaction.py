from models.transaction import Transaction


def test_to_dict():
    t = Transaction(50.0, "groceries", "2026-06-22", "weekly shop")
    assert t.to_dict() == {
        "amount": 50.0,
        "category": "groceries",
        "date": "2026-06-22",
        "description": "weekly shop",
    }
