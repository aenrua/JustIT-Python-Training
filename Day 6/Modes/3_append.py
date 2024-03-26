
# a for adding to an existing file​ and creates the file if it does not exists
# Using context manager to handling resource usage
" automatically setup and teardown resources"

"Syntax :  with openMethod('pathtofolder/pathtofile/fileName.txt', 'w') as varName:"
with open('Day 6/file2.txt',"a") as filePath1:
    contents = "\nI\nam\nAnton" #"\nYourA\ntext\ngoes\nhere\nin\nnewlines"
    filePath1.write(contents) #write to file 


"To Do: Task 1: Task 1: Refer to the example code above to use the context manager to:"
# append to your file (yourName.txt), your interests and a fake address
with open('Day 6/Modes/Anton.txt',"a") as filePath2:
    contents = "\nGaming, Volleyball, Snowboarding\nHampton, London"
    filePath2.write(contents)

"Further reading"
# https://www.w3docs.com/snippets/python/how-to-read-a-text-file-into-a-list-or-an-array-with-python.html