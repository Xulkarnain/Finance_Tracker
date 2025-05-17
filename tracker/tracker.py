import json

class Tracker:
    def read_transactions(self, filepath='D:\\Btech_CS\\Finance_tracker\\transactions.json'):
        transactions = []
        try:
            with open(filepath, 'r') as file:
                for line in file:
                    transactions.append(json.loads(line.strip()))
        except FileNotFoundError:
            print("No transactions found.")
        return transactions

    def display_transactions(self):
        data = self.read_transactions()  # ✅ use self and no need to pass argument

        if not data:
            print("No transactions found.")
            return

        print(f"\n{'TYPE':<10} {'CATEGORY':<15} {'AMOUNT':<10} {'DATE'}")
        print("-" * 60)
        for item in data:
            print(f"{item['type']:<10} {item['category']:<15} {item['amount']:<10} {item['date']}")
