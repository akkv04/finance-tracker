from models.transaction import Transaction
from storage.json_store import save_transaction, load_transaction


def test_save_load_roundtrip(tmp_path):
    file_path = tmp_path / "transactions.json"
    originals = [
        Transaction(50.0, "groceries", "2026-06-22", "weekly shop"),
        Transaction(12.0, "coffee", "2026-06-23", "latte"),
    ]

    save_transaction(originals, str(file_path))
    loaded = load_transaction(str(file_path))

    assert len(loaded) == 2
    assert loaded[0].category == "groceries"
    assert loaded[0].amount == 50.0
    assert loaded[1].category == "coffee"
    assert loaded[1].amount == 12.0


def test_load_missing_file_returns_empty_list(tmp_path):
    missing_path = tmp_path / "does_not_exist.json"
    assert load_transaction(str(missing_path)) == []
