# Question 3 :
# Scenario: Manage a collection of items using Python's list data structure.
#   ● Task 3.1: Initialize an empty list named shopping_cart.
#   ● Task 3.2: Use a for loop that runs 5 times. Inside the loop, ask the user for an item and append it to the list.
#   ● Task 3.3: Use the len() function to print how many items are in the cart.
#   ● Task 3.4: Sort the list alphabetically and print the result.
#   ● Task 3.5: Check if the string "Milk" is present in the list using an if statement. Print a custom reminder if it is found.

shopping_cart = []

for _ in range(5):
    item = input('Enter item: ')
    shopping_cart.append(item)
    
print(f'Total no. items: {len(shopping_cart)}')

shopping_cart.sort()

print(f'Items in shopping cart: {shopping_cart}')

print('Found' if 'milk' in shopping_cart else 'Not found')
