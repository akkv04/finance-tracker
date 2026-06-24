import json

class Transaction:

    def __init__(self, amount:float, category:str, date, description):
        self.category = category
        self.amount = amount
        self.date = date
        self.description = description

    def to_dict(self):
        return{
            "amount":self.amount,
            "category": self.category,
            "date":self.date,
            "description":self.description
        }
    def __repr__(self):
        return f"Transaction(amount:{self.amount}, category: {self.category}, date: {self.date}, description:{self.description} )"
    