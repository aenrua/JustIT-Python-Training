"""use a while loop when the number of iteration is unknown(dont know how many times you want/going 
to do something for)
A while loop also controls the flow of execution in a program"""



# import the datetime library/class/module
import datetime


"To Do: Predict, then Run, and then Investigate"



print("None while Loop output")
dateTime = datetime.datetime.now()
print(dateTime.strftime("%H:%M:%S"))


"To Do: Task 1" 
" study the output of the code above and the output in the while loop below, and use the links provided to answer"

" What is the while loop doing?"
# Answer: while the loop is running, print the current time

" add comment to explain what you understand the 'datetime.datetime.now().strftime('%H:%M:%S')'"
# Answer: datetime module, datetime class, the current time, the string format of time

" add comment to explain what you understand the 'end='"
# https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/
# Answer: Ends the print function

" add comment to explain what you understand the '\r' "
# https://www.w3schools.com/python/gloss_python_escape_characters.asp
# Answer: \r is a carriage return

" add comment to explain what you understand the 'end=' is used for"
# Answer: Ending the print function at the end of the line instead of the new line

" add comment to explain what you understand the '\r' is used for "
# Answer: It tells Python to move the cursor back to the beginning of the current line

" What will output if you remove  , end='\r'  from the while loop"
# Answer: Several lines of the current time being printed infinitely. The \r makes it so that the code only prints 1 line and updates it

print("while Loop output")
while True:
    print(datetime.datetime.now().strftime("%H:%M:%S"), end="\r")

    # time.sleep(1)

"Further reading on python while statements"
# https://www.w3schools.com/python/ref_keyword_while.asp
# https://www.w3schools.com/python/python_ref_keywords.asp
# https://www.w3schools.com/python/python_reference.asp