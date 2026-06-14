# Question 5 :
# Scenario: Store and manipulate structured data for a classroom.
#   ● Task 5.1: Create a dictionary where the Key is a student's name (string) and the Value is a tuple containing their (Age, Major). Add at least 3 students.
#   ● Task 5.2: Create a Set containing all the unique Majors from the dictionary. (Note: Since sets don't allow duplicates, this will show you how many distinct subjects are being studied).
#   ● Task 5.3: Use a for loop to iterate through the dictionary and print a sentence for each student: "Student [Name] is [Age] years old and is majoring in [Major]."
#   ● Task 5.4: Update the Major of one student in the dictionary and print the final dictionary to verify the change.

students = {
    'adarsh': (21, 'mechanical'),
    'athul': (20, 'computer science'),
    'deepu': (19, 'mathematics'),
}

majors = set(major for age,major in students.values())

print('Before Change')
for name, (age, major) in students.items():
    print(f'Student {name} is {age} years old and is majoring in {major}.')
    
students['athul'] = (21, 'computer hardware')
    
print('After Change')
for name, (age, major) in students.items():
    print(f'Student {name} is {age} years old and is majoring in {major}.')
