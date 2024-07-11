# Expense Budget Tracker

The Expense Budget Tracker is a simple console-based application designed to help users manage their personal finances effectively. This tool allows users to track their income and expenses, view summaries of their financial activities, and analyze their spending patterns by category.

## Features

- **Add Income/Expense:**
  - Record entries for income or expenses.
  - Specify the amount and category (e.g., salary, groceries, entertainment).
  - Automatically updates the total income, total expenses, and net balance.

- **View Summary:**
  - Display total income, total expenses, and net balance.
  - Break down income and expenses by category, showing the total amount for each category.
  - Provides a clear overview of financial status and spending habits.

- **User-Friendly Interface:**
  - Simple text-based menu for easy navigation.
  - Clear prompts and feedback messages to guide users through the process.

## Usage

1. **Add Income/Expense:**
   - Select option `1` from the main menu.
   - Enter the amount, category, and type (income or expense).
   - Ensure the amount is positive and the type is either 'income' or 'expense'.

2. **View Summary:**
   - Select option `2` from the main menu.
   - View the total income, total expenses, and net balance.
   - Review the breakdown of income and expenses by category.

3. **Quit:**
   - Select option `3` from the main menu to exit the application.

## Example Usage

```plaintext
--- Personal Budget Tracker ---
1. Add Income/Expense
2. View Summary
3. Quit
Enter your choice (1/2/3): 1
Enter the amount: 500
Enter the category (e.g., salary, groceries, entertainment): salary
Enter the type (income/expense): income
Entry added successfully!

--- Personal Budget Tracker ---
1. Add Income/Expense
2. View Summary
3. Quit
Enter your choice (1/2/3): 2

--- Budget Summary ---
Total Income: $500.00
Total Expenses: $0.00
Net Balance: $500.00

Income Breakdown by Category:
salary: $500.00

Expense Breakdown by Category:
```

## Requirements

- Python 3.x

## How to Run

1. Ensure you have Python 3.x installed on your system.
2. Copy the code into a file named `budget_tracker.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory where `budget_tracker.py` is saved.
5. Run the script using the command: `python budget_tracker.py`.

## Future Enhancements

- Adding a feature to save and load data from a file.
- Implementing graphical user interface (GUI) for a better user experience.
- Adding more detailed analytics and charts.
