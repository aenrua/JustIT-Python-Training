"""use a while loop when the number of iteration is unknown(dont know how many times you want/going 
to do something for)
A while loop also controls the flow of execution in a program"""


num = 1


"To Do: Explain what is += 1  ?"

"Modify/Make"
"To Do: Task 2: Modify the whileloop above to count down from 20 to 1 and comment your code"

num = 20
while num <= 20:  # start from 1 and keep looping to 20(condition is met)
    print(num)
    if num == 1:  # check if the value in userNum is the same as the value in num
        break  # break/exit the loop
    num -= 1
