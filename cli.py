import argparse
from models.transaction import Transaction
from storage.json_store import save_transaction,load_transaction

file_path ="abc.json"

def handle_add(args):
    tran_list = load_transaction(file_path)
    new_tran = Transaction(args.amount, args.category, args.date, args.descr)
    tran_list.append(new_tran)
    save_transaction(tran_list,"abc.json")

def handle_list(args):
    tran_list= load_transaction(file_path)
    print(tran_list)


def calculate_summary(tran_list):
    totals = {}
    for t in tran_list:
        totals[t.category] = totals.get(t.category, 0) + t.amount
    return totals


def handle_summary(args):
    tran_list = load_transaction(file_path)
    totals = calculate_summary(tran_list)
    for category, total in totals.items():
        print(f"{category}: {total}")


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("amount", type = float)
    add_parser.add_argument("category", type = str )
    add_parser.add_argument("date")
    add_parser.add_argument("descr",type=str)
    add_parser.set_defaults(func=handle_add)

    list_parser = subparsers.add_parser("list")
    list_parser.set_defaults(func=handle_list)

    summary_parser = subparsers.add_parser("summary")
    summary_parser.set_defaults(func = handle_summary)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()

