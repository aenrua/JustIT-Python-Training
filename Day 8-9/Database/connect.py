import sqlite3 as sql # import the sqlite3 module and assign it an alias

try:
    # to use the sqlite(SQL) module, we start by creating a variable(object) to hold the path to the folder(file)
    with sql.connect("Day 8-9/Database/dfe6w4.db") as dbCon: # use connect function to open folder path, then file
        # use to execute the SQL statement with the execute method
        dbCursor = dbCon.cursor()
except sql.OperationalError as e: # raise SQL error
    # handling the error
    print(f"Connection Failed: {e}")