import time
import json
import os

class Transaction:
    def __init__(self, amount, type, category):
        self.date = time.ctime()
        type = type.lower()
        if type == "income" or type == "expense":
            self.amount = int(amount)
            self.type = type
            self.category = category
        else:
            raise ValueError("Transaction type must be 'income' or 'expense'")
        
        print("Transaction Done")
        
        
        
    def to_dict(self):
        return {
            "type": self.type,
            "category": self.category,
            "amount": self.amount,
            "date": self.date
        }
        
    def save_to_json(self):
        with open("transactions.json", "a+") as f:
            json.dump(self.to_dict(), f)
            f.write("\n")

    def savings(self):
        transactions = []
        try:
            with open("transactions.json", "r") as file:
                for line in file:
                    transactions.append(json.loads(line.strip()))
        except FileNotFoundError:
            print("No transactions found.")

        total_income = 0
        total_expense = 0
        for transaction in transactions:
            if transaction["type"] == "income":
                total_income += transaction["amount"]
            elif transaction["type"] == "expense":
                total_expense += transaction["amount"]

        self.saving = total_income - total_expense
        return self.saving

