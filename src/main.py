class Expense:
    """Add a new expense: amount, date, category, description"""
    def __init__(
        self,
        amount: int,
        date: str,
        category: str,
        description: str
    ) -> None:

        self.amount = amount
        self._date = date
        self._category = category
        self._description = description

    @property
    def amount(self) -> int:
        return self._amount

    @amount.setter
    def amount(self, value: int) -> None:
        if value < 0:
            raise ValueError("Expense amount cannot be negative")
        self._amount = value

    @property
    def date(self) -> str:
        return self._date

    @property
    def category(self) -> str:
        return self._category

    @property
    def description(self) -> str:
        return self._description

    def __str__(self) -> str:
        return f"Amount: {self.amount} | Date: {self.date} | Category: {self.category} | Description: {self.description}"


class ExpenseService:
    """Services"""
    def __init__(self):
        self.expenses: list[Expense] = []

    def add_expense(self, expense: Expense) -> None:
        self.expenses.append(expense)

    def remove_expense(self, index: int) -> str:
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            return ""
        else:
            return "Invalid number!"

    def view_expenses(self) -> str:
        if len(self.expenses) == 0:
            return "No expenses!"

        else:
            all_expenses = "\n---------- All Expenses ----------\n"
            for i, e in enumerate(self.expenses, start=1):
                all_expenses += f"{i}. {e}\n"
            return all_expenses

    def total_expenses(self) -> str:
        if len(self.expenses) == 0:
            return "No expenses!"

        else:
            categories = dict()
            text = ""

            for e in self.expenses:
                if e.category not in categories:
                    categories[e.category] = e.amount

                else:
                    categories[e.category] += e.amount

            for k, v in categories.items():
                text += f"{k}: {v}\n"

            all_sum = 0
            for e in self.expenses:
                all_sum += e.amount

            text += "------------------------------\n"
            text += f"Total Expenses: {all_sum}"

            return text


def main():
    """Main function of the project"""
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
                    index = int(input("Enter your number: "))
                    break
                except ValueError:
                    print("Enter a number.")

            print(tracker.remove_expense(index - 1))

        elif choice == "3":
            print(tracker.view_expenses())

        elif choice == "4":
            print(tracker.total_expenses())

        elif choice == "5":
            print("\n--- Thank you for using our application. Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()