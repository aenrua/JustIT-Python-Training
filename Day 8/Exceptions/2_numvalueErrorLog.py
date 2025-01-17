import logging

"To Do: Predict, then Run, and then Investigate"
#different logging methods and severity
logging.basicConfig(filename=r"Day 8\Exceptions/file2.log", level=logging.DEBUG) 

try:  # attempt to run the indented code block
    num1 = int(input(("Enter your first number: ")))
    num2 = int(input(("Enter your second number: ")))
    answer = num1 / num2

    #Output for developer/what the developer sees
    logging.info(f"Divided {num1} / {num2} = {answer}")

    #Output for user/what the user sees
    print(f"You have divided {num1} / {num2} = {answer}")

except ZeroDivisionError:  # handles exception if code in try block fails
    #Output for user/what the user sees
    print("You can't divide a number by zero")

    #Output for developer/what the developer sees
    logging.warning("User attempted to divide by zero")

finally:
    print("Closing....")



"To Do: Task 1: Modify"
# Make: 
# 1. Use any one of the logging methods to log error to the Exceptions folder in a file called myFilelog1.log 
