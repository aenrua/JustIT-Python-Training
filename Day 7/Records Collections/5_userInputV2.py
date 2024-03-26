fname    = input("Enter you full name: ")
address   = input("Enter your address: ")
interest = input("Enter your interest: ")
age      =    int(input("Enter your age: "))


# create a dictionary
userData = {
    "Fullname":fname,
    "Address":address,
    "Interest":interest,
    "Age":age
    }


with open('Day 7/Records Collections/userDetails1.txt', 'a') as addData:
    for aKey, aValue in userData.items():
        addData.write(f"Key: {aKey}, Value: {aValue}")



"Further reading"
# https://www.w3schools.com/python/python_file_handling.asp