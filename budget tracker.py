class BudgetTracker:
    def _init_(self):
        self.categories = {}

    def add_category(self, category_name):
        if category_name not in self.categories:
            self.categories[category_name] = 0
            print(f"{category_name} category added.")
        else:
            print("Category already exists.")

    def add_expense(self, category_name, amount):
        if category_name in self.categories:
            self.categories[category_name] += amount
            print(f"${amount} added to {category_name} category.")
        else:
            print("Category does not exist.")

    def get_total_spent(self):
        total = sum(self.categories.values())
        return total

    def view_categories(self):
        for category, amount in self.categories.items():
            print(f"{category}: ${amount}")


def main():
    budget_tracker = BudgetTracker()

    while True:
        print("\n1. Add Category\n2. Add Expense\n3. View Categories\n4. View Total Spent\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            category_name = input("Enter category name: ")
            budget_tracker.add_category(category_name)
        elif choice == '2':
            category_name = input("Enter category name: ")
            amount = float(input("Enter amount: "))
            budget_tracker.add_expense(category_name, amount)
        elif choice == '3':
            budget_tracker.view_categories()
        elif choice == '4':
            total_spent = budget_tracker.get_total_spent()
            print(f"Total Spent: ${total_spent}")
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "_main_":
    main()