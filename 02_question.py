# Question 2 :
# Scenario: Simulate a vending machine that offers different variations of drinks.
#   ● Task 2.1: Ask the user to choose a drink from three options: Soda, Coffee, or Water.
#   ● Task 2.2: Use nested conditions to provide sub-options:
#       ○ If Soda: Ask if they want "Regular" or "Diet".
#       ○ If Coffee: Ask if they want "With Sugar" or "Black".
#       ○ If Water: Ask if they want "Still" or "Sparkling".
#   ● Task 2.3: Use an else statement to catch invalid inputs (e.g., if the user types "Juice").
#   ● Task 2.4: Print a final confirmation message: "Dispensing your [Sub-option] [Drink Choice]!"

_soda_ = 'soda'
_coffee_ = 'coffee'
_water_ = 'water'

print('-- Menu Items --')
main_option = input('1. Soda\n2. Coffee\n3. Water\nEnter the choice:').lower()

if main_option == _soda_:
    sub_option = input('Sub-Options\n1. Regular\n2. Diet\nSelect one:')
elif main_option == _coffee_:
    sub_option = input('Sub-Options\n1. With Sugar\n2. Black\nSelect one:')
elif main_option == _water_:
    sub_option = input('Sub-Options\n1. Still\n2. Sparkling\nSelect one:')
else:
    print('Invalid inputs')
    
print(f'Dispensing your {sub_option} {main_option}!')
