# fname    = input("Enter you full name: ")
# address   = input("Enter your address: ")
# interest = input("Enter your interest: ")
# age      =    int(input("Enter your age: "))


# create a dictionary 
dict1 = {"Fullname": "Jane Smith", "Age": 23, "Hobby":"Coding", 1:"Gamer"}

# create a dictionary with keys but no values 
print("dictionary with keys but no values")
userDetails1 = {"fname": "", "address": "", "interest":"", "age":""}
print(userDetails1)

"Adding values to dictionary"
# Method 1 - Manual input
# Use key to add values to dictionary 
# userDetails1["fname"] = input("Enter your full name: ")
# print(userDetails1)
# userDetails1["address"] = input("Enter your address: ")
# print(userDetails1)
# userDetails1["interest"] = input("Enter your interest: ")
# print(userDetails1)
# userDetails1["age"] = input("Enter your age: ")
# print(userDetails1)
# print("End of Manual input\n")

# Method 2 - For loop input
# create a for loop to add data to dictionary
# for keyVal in userDetails1: # iterate or loop through all keys and values
#     userDetails1[keyVal] = input(f"Enter the value for {keyVal}: ")
# print(userDetails1)


"Extension"
"Modify"
"To Do: Task 1: write the input statement to add the remaining values to the userDetails1 dictionary above"

# create a dictionary with no keys and no values 
print("dictionary with no keys and no values")

"Make"
"To Do: Task 2: Create a dictionary with no keys as shown below, then write the input statement to add the keys and values."
userDetails2 = {}
print(userDetails2)

numOfKeyVal = int(input("Enter the number of key value pairs: "))
keyValCount = 0 # counter

while True:
    aKey = input("Enter the key")
    aValue = input(f"Enter the value for {aKey}: ")
    userDetails2[aKey] = aValue
    keyValCount +=1 # increase counter by 1
    # check if the numOfKeyVal is the same as keyValCount
    if keyValCount == numOfKeyVal:
        break
print(userDetails2)