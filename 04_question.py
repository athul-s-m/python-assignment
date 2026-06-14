# Question 4 :
# Scenario: Create a game where the user must guess a predefined "Secret Number."
#   ● Task 4.1: Hardcode a variable secret_number with any integer (e.g., 42).
#   ● Task 4.2: Initialize a variable attempts = 0.
#   ● Task 4.3: Create a while loop that continues until the user's input matches the secret_number.
#   ● Task 4.4: Inside the loop:
#       ○ Increment the attempts counter by 1 for every guess.
#       ○ Provide feedback: Tell the user if their guess is "Too High" or "Too Low."
#   ● Task 4.5: Once the loop ends (the guess is correct), print a congratulatory message showing the total number of attempts.

secret_number = 42
attempts = 0

while attempts == 0 or input_number != secret_number:
    input_number = int(input('Guess a number: '))
    
    if input_number > secret_number:
        print('Too High')
    elif input_number < secret_number:
        print('Too Low')
        
    attempts += 1
    
print('Congrajulations You Found!!!')
