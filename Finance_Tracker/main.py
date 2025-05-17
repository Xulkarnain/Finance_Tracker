from tracker.transaction import Transaction
from tracker.tracker import Tracker


while True:
    print("\n==== Transaction Manager ====")
    print("1. Add a new transaction")
    print("2. View all transactions")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
            a = Transaction(
            input("Enter amount: "),
            input("Enter type (income/expense): "),
            input("Enter category: ")
            )
            a.save_to_json()

            print("Total savings : " , a.savings())
            
    elif choice == '2':
        Tracker().display_transactions()
    elif choice == '3':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

