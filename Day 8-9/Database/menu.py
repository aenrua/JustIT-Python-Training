import readSongs, addSongs, updateSongsV2, deleteSongs, reportsV2

def read_file(file_path): # file_path is a parameter/variable
    try:
        with open(file_path) as readFile:
            rf = readFile.read()
            return rf
    except FileNotFoundError as nf:
        print(f"File not found because: {nf}")
# test to retrieve or load menuOptions.txt
# print(read_file("Day 8/Database/menuOptions.txt"))

def songs_menu():
    option = 0 # initialise/assign the option variable with an integer value 0
    # create a list of string values/elements/items
    optionsList = ["1","2","3","4","5","6"]
    # call the read file function and assign it to a variable
    menuChoices = read_file("Day 8-9/Database/menuOptions.txt")

    # repeat the menu options until the option to exit the menu is entered
    while option not in optionsList:
        # print the menuoptions by calling the variable that holds the read_file
        print(menuChoices)

        #re-assign the value of the option variable so it can be re-used
        option = input("Enter an option from the menu choices above: ") # 1 = "1" or 2 = "2"
        
        # check if the input entered in the option variable above is not outside of or within range of 1,2,3,4,5,6
        if option not in optionsList:
            print(f"{option} is not a valid choice!")
    return option

mainProgram = True # Toggle to False to exit the while loop below
while mainProgram: # same as while True
    # call the songs_menu() function and assign it to a variable
    mainMenu = songs_menu()

    # match case is the equivalent of switch statements in JS
    match mainMenu:
        case "1": # call the readSong file imported on line 1 and the function inside of it called read_songs()
            readSongs.read_songs()
        case "2":
            addSongs.insert_song()
        case "3":
            updateSongsV2.update_song()
        case "4":
            deleteSongs.delete_song()
        case "5":
            reportsV2.search_song()
        case _:
            mainProgram = False # set the mainProgram to False to exit the menu
input("Press enter to exit the...")