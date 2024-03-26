# Selection is used to control the flow of the program

pStudy = input("Enter your program of study: ").title()
curProgram = "Bootcamp"

"Predict, then Run, and then Investigate"

# check the condition that pStudy value is same as the value held in curProgram

# do something/execute the line of code if the condition is checked above true/met - welcome

# The block(else) of code will be executed if the condition in the if block is not true/not met

if pStudy == curProgram:
    print("Welcome")
else:
    print("Not welcome")


"Modify"
#ToDo: Exercise
# Modify the code above to use the "!=" operator, or the "not" operator

if pStudy != curProgram:
    print("What are you doing here?")
else:
    print("Welcome")


"Your Turn to: Apply and Build"

"Task 1: Using if and else"
# 1. Create a program that finds the minimum value between two numbers using if else

num1 = float(input("Number 1: "))
num2 = float(input("Number 2: "))

if num1 < num2:
    print(f"{num1} is smaller than {num2}")
else:
    print(f"{num2} is smaller than {num1}")


"Task 2"
# 2.Create a python program to check user's password and print "Logged In" if successful
# else "Not Logged In“ when unsuccessful.

password = input("Password: ")
userPassword = "MyPassword"

if userPassword == password:
    print("Logged In")
else:
    print("Not Logged In")