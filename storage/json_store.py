from models.transaction import Transaction
import json

def save_transaction(tran:list, filepath:str):
    data = [t.to_dict() for t in tran]
    with open(filepath,"w") as f:
        json.dump(data, f, indent=2)

def load_transaction(filepath:str):
    with open(filepath,"r") as f:
        ouptut= json.load(f)
        print (ouptut)