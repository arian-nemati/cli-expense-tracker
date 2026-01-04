class Expense:
    """Add a new expense: amount, date, category, description"""

    def __init__(self, amount, date, category, description):
        self.amount = amount
        self.date = date
        self.category = category
        self.description = description


class ExpenseService:
    """Services"""

    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
        else:
            print("Invalid index")

    def view_expenses(self):
        if len(self.expenses) == 0:
            print("No expenses!")

        else:
            print("\n--- All Expenses ---")
            for i, e in enumerate(self.expenses, start=1):
                print(f"{i}. Amount: {e.amount}, Date: {e.date}, Category: {e.category}, Description: {e.description}")

    def total_expenses(self):
        if len(self.expenses) == 0:
            print("No expenses!")

        else:
            categories = dict()

            for e in self.expenses:
                if e.category not in categories:
                    categories[e.category] = e.amount

                else:
                    categories[e.category] += e.amount

            for k, v in categories.items():
                print(f"{k}: {v}")

            all_sum = 0
            for e in self.expenses:
                all_sum += e.amount

            print("--------------")
            print(f"Total Expenses: {all_sum}")


def main():
    tracker = ExpenseService()

    while True:
        print("\nWelcome to Expense Tracker. Choose an option: ")
        print("1. Add a new expense")
        print("2. Remove an expense")
        print("3. View all expenses")
        print("4. Total expenses")
        print("5. Quit")
        choice = input("Enter your choice number (1-5): ")

        if choice == "1":
            while True:
                try:
                    amount = int(input("Enter your amount: "))
                    break
                except ValueError:
                    print("Invalid amount.")

            date = input("Enter your date (YYYY-MM-DD): ")
            category = input("Enter your category: ")
            description = input("Enter your description: ")
            my_expense = Expense(amount, date, category, description)
            tracker.add_expense(my_expense)

        elif choice == "2":
            while True:
                try:
                    index = int(input("Enter your index: "))
                    break
                except ValueError:
                    print("Enter a number.")

            tracker.remove_expense(index)

        elif choice == "3":
            tracker.view_expenses()

        elif choice == "4":
            tracker.total_expenses()

        elif choice == "5":
            print("\nThank you for using our application. Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()