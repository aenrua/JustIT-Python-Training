# num1 = int(input(("Enter your first number: ")))
# num2 = int(input(("Enter your second number: ")))
# answer = num1 / num2

# print(answer)
# print("Execute the following code...\n...\n......\n...\n...")

try: # test run or try the code within the try block
    num1 = int(input(("Enter your first number: ")))
    num2 = int(input(("Enter your second number: ")))
    answer = num1 / num2
    print(answer)

except ZeroDivisionError: # handle the exception (ensure the program does not break)
    print("Are you trying to break the universe!? NEVER DIVIDE BY ZERO")

finally:
    print("Operation completed")

print("Execute the following code...\n...\n......\n...\n...")