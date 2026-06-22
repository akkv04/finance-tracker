class Transaction:
    def __init__(self,amount: float, category: str, date, description: str):
        self.amount = amount
        self.category = category
        self.date= date
        self.description=description

    def to_dict(self):
        return{
            "amount":self.amount,
            "category":self.category,
            "date":self.date,
            "description":self.description
        }
    
    def __repr__(self):
        return f"Tranaction(amount:{self.amount},category:{self.category},date:{self.date},description:{self.description})"