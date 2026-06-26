# financetracker

A simple command-line expense tracker. Log transactions to a local JSON file, list them, and see a quick spending summary by category.

## Install

```bash
git clone <this-repo-url>
cd financetracker
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

### Add a transaction

```bash
python cli.py add <amount> <category> <date> <description>
```

```bash
python cli.py add 42.50 groceries 2026-06-22 "Trader Joe's"
```

### List all transactions

```bash
python cli.py list
```

### Show a spending summary by category

```bash
python cli.py summary
```

Transactions are stored in `abc.json` in the project root (created automatically on the first `add`).

## Example run

```
$ python cli.py add 42.50 groceries 2026-06-22 "Trader Joe's"

$ python cli.py add 15.00 coffee 2026-06-23 "Latte"

$ python cli.py add 60.00 groceries 2026-06-24 "Costco run"

$ python cli.py list
[Transaction(amount:42.5, category: groceries, date: 2026-06-22, description:Trader Joe's ), Transaction(amount:15.0, category: coffee, date: 2026-06-23, description:Latte ), Transaction(amount:60.0, category: groceries, date: 2026-06-24, description:Costco run )]

$ python cli.py summary
groceries: 102.5
coffee: 15.0
```

## Running tests

```bash
pip install pytest
pytest
```
