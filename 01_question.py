# Question 1 :
# Scenario: Create a tool to help a user understand their monthly spending habits.
#   ● Task 1.1: Prompt the user to input their Monthly Salary, Rent, Food Expenses, and Utility Costs.
#       ○ Ensure these inputs are treated as numbers (floats/integers).
#   ● Task 1.2: Calculate the Total Expenses (Rent + Food + Utilities) and the Remaining Balance (Salary - Total Expenses).
#   ● Task 1.3: Calculate the Percentage of the salary spent specifically on Rent.
#       ○ Formula: (Rent / Salary) * 100
#   ● Task 1.4: Print a formatted summary showing the total spent, the balance left, and the rent percentage rounded to two decimal places

def user_input() -> dict:
    while True:
        try:
            print('---Expense Calulator---')
            salary = float(input('Enter monthly salary: '))
            rent = float(input('Enter monthly rent: '))
            food_expense = float(input('Enter monthly food expense: '))
            utility_cost = float(input('Enter monthly utility cost: '))
        except ValueError:
            print('!!!Try to enter numerical values!!!')
        else:
            return {
                'salary': salary, 
                'rent': rent, 
                'food_expense': food_expense, 
                'utility_cost': utility_cost
            }
            
def user_input_handler() -> list:
    user_data = user_input()
    salary = user_data["salary"]
    rent = user_data["rent"]
    food_expense = user_data["food_expense"]
    utility_cost = user_data["utility_cost"]
    return [salary, rent, food_expense, utility_cost]

def calculate_balance(income: float, expense: float) -> float:
    return income - expense

def calculate_percentage(amount: float, total_amount: float) -> float:
    try:
        percentage = amount / total_amount * 100
    except ZeroDivisionError:
        return -1
    return percentage

def calculate_expense(*expenses: float) -> float:
    return sum(expenses)

def formatted_summary(expense: float, 
                      balance: float, 
                      rent_percentage: float) -> None:
    print('\n---Summary---')
    print(f'Total Spent\t: ${expense:.2f}')
    print(f'Balance\t\t: ${balance:.2f}')
    print(f'Rent percentage\t: {rent_percentage:.2f}%')
    
def main():
    salary, rent, food_expense, utility_cost = user_input_handler()
    
    total_expense = calculate_expense(rent, food_expense, utility_cost)
    balance = calculate_balance(salary, total_expense)
    rent_percentage = calculate_percentage(rent, salary)
    
    formatted_summary(total_expense, balance, rent_percentage)
    
if __name__ == '__main__':
    main()
