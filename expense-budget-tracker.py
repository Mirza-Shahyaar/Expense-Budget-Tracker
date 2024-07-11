total_income = 0
total_expenses = 0
net_balance = 0

income_entries = []
expense_entries = []

while True:
    print("\n--- Personal Budget Tracker ---")
    print("1. Add Income/Expense")
    print("2. View Summary")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        amount = float(input("Enter the amount: "))
        category = input("Enter the category (e.g., salary, groceries, entertainment): ")
        entry_type = input("Enter the type (income/expense): ").lower()

        if amount <= 0:
            print("Amount must be positive.")
            continue

        if entry_type == "income":
            total_income += amount
            income_entries.append((amount, category))
        elif entry_type == "expense":
            total_expenses += amount
            expense_entries.append((amount, category))
        else:
            print("Invalid type. Please enter either 'income' or 'expense'.")
            continue

        net_balance = total_income - total_expenses
        print("Entry added successfully!")

    elif choice == '2':
        print("\n--- Budget Summary ---")
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Net Balance: ${net_balance:.2f}\n")
        
        print("Income Breakdown by Category:")
        income_summary = {}
        for amount, category in income_entries:
            if category in income_summary:
                income_summary[category] += amount
            else:
                income_summary[category] = amount
        for category, total in income_summary.items():
            print(f"{category}: ${total:.2f}")
        
        print("\nExpense Breakdown by Category:")
        expense_summary = {}
        for amount, category in expense_entries:
            if category in expense_summary:
                expense_summary[category] += amount
            else:
                expense_summary[category] = amount
        for category, total in expense_summary.items():
            print(f"{category}: ${total:.2f}")

    elif choice == '3':
        print("Exiting the budget tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
