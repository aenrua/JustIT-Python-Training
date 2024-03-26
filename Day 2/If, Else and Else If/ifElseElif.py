# Selection is used to control the flow of the program

# elif == else if

score = int(input("Enter a number: "))
"Predict, then Run, and then Investigate"
# check the condition that score is greater than 100
if score > 100:
# create a variable and assign it the value Invalid Entry
    grade = "Invalid Entry"
# check the condition that score is between 75 and 100
elif score <=100 and score >=75:
# create a variable and assign it the value A
    grade = "A"
# check the condition that score is between 60 and 74
elif score <=74 and score >=60:
# reassign the grade variable the value B
    grade = "B"
# check the condition that score is between 50 and 59
elif score <=59 and score >=50:
# reassign the grade variable the value C
    grade = "C"
# reassign the grade variable the value F
else:
    grade = "F"

print(grade)

#ToDo: Q&A
"What do you think is the equivalent of JS else if in python?"


"Make"
#ToDo: Task 1: Using if elif and else
# Create a Menu program that allows users to select between three subject choices
# User must be presented with the value associated with each choice
# for example 1. Music, 2. Maths ....
# A choice must also be available for the user to exit the program
# A message using the print function must be displayed as per the user choice

subject1 = "Maths"
subject2 = "English"
subject3 = "Science"
print(f"Subject options - 1. {subject1} | 2. {subject2} | 3. {subject3}")
userSubject = input("Please choose a subject: ").title()
if userSubject == subject1:
    response = "You have chosen Maths"
elif userSubject == subject2:
    response = "You have chosen English"
elif userSubject == subject3:
    response = "You have chosen Science"
else:
    response = "Please select a subject from the choices above."
print(response)


#ToDo: Task 2
# Use if else to find item(a specific number) from a list
numList = [56, 78, 100, 45, 88, 71]
