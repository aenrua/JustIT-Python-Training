
"As your programs become larger and more complex, they need to be broken down into smaller, self-contained sections"
"In python function is a type of subroutine, a subroutine is sequence of instructions to perform a specific task with an identifiable name."

"A subroutine(function) definition is used to define the steps within the subroutine(function)"

"A subroutine(function) may or may not have a return statement"

"A subroutine(function) may or may not have parameters"

"def just defines the subroutine(function)"

"A subroutine(function) is not executed unless the subroutine is called."

"A subroutine(function) call tells the program to branch to the function, execute it and come back to the next statement in the main program"

"Custom built function"  '' # A function that you have created yourself and imported into other programs that you have created.

# Syntax
"""
def subroutine/functionName():
    subroutine/functionBody(code)
    subroutine/functionBody(code)
    subroutine/functionBody(code)
    subroutine/functionBody(code)

#call/invoke the subroutine/function
subroutine/functionName()


"""

"To Do: Predict, then Run, and then Investigate"
# name is a global variable 
name = "Emjay"
print("Your name is: ", name)

name= input("What is your name? ")
print("Your name is: ", name)


# def define the subroutine/function user

# name is a now a local variable 
name = ""

# def define the subroutine userName
def userName():
    print(f'Welcome {name}')

# print("Welcome")
userName()

"To Do: Task 1: Call the subroutine inside a print function with or without f-strings and explain your result"
print("Subroutine call: ", end="")
userName()

"Modify/Make"
"To Do: Task 2: Modify the subroutine to ask for address and interest"
def userName2():
    name = input("What is your name? ")
    address = input("Where do you live? ")
    interests = input("What are your interests? ")
    print(f'Welcome {name}! Your address is {address} and your interests are {interests}')

print("Please answer the questions below.\n", end="")
userName2()

'Task 2: Investigate  if __name__ == "__main__":'
'Copy and paste the code block above if __name__ == "__main__":  in the browser to investigate it use'
# if __name__ == "__main__":
# Add comment to explain why it can be used in your program in your own words"
# Answer: Allows you to execute code when the files runs as a script, but not when it's imported

# call/invoke the subroutine
# call/invoke the subroutine

"Knowledge Check"
"Task 4: Linking existing knowledge with new knowledge"
# What do you think is the equivalent of the python 'def' keyword in JavaScript
# Answer: function

"Further reading on python functions"
# 

def age():
    print(3)

def address():
    print("London")
