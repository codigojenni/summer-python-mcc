import locale as lc

lc.setlocale(lc.LC_ALL, "en_US")

# s1 and s2 variables like future value program from ch 9
s1 = 20
s2 = ".2f"

def get_income():
    while True:
        try:
            income = float(input("Enter your monthly income: "))
            if income < 0:
                raise ValueError("Income must be zero or more.")
            return income
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_expense_list():
    expenses = []
    print("\nEnter your expenses one at a time.")
    print("Enter 0 when finished.\n")

    while True:
        try:
            amount = float(input("Enter an expense amount: "))
            if amount == 0:
                break
            if amount < 0:
                raise ValueError("Expense must be zero or more.")
            expenses.append(amount)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return expenses

def show_budget(income, expenses):
    total_expenses = sum(expenses)
    remaining = income - total_expenses

    print()
    print(f"{'Total Income:':{s1}} ${income:{s2}}")
    print(f"{'Total Expenses:':{s1}} ${total_expenses:{s2}}")
    print(f"{'Remaining Budget:':{s1}} ${remaining:{s2}}")
    print()

    print("Complete Expense List")
    print("-------------------------------------")
    for i, amount in enumerate(expenses, start=1):
        print(f"{i}. ${amount:{s2}}")

def main():
    choice = "y"
    while choice.lower() == "y":
        print("\nWelcome to the Budget Tracker")
        print("------------------------------------------")

        income = get_income()
        expenses = get_expense_list()
        show_budget(income, expenses)

        choice = input("\nWould you like to enter another budget? (y/n): ")
    
    print("\nCompleted by, Jennifer Mendoza Trejo")

if __name__ == "__main__":
    main()
