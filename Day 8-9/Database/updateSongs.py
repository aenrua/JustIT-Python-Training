from connect import *

def update_song():
    try:
        # SongID is primary key field
        songID = int(input("Enter the SongID of the record to be updated: "))
        dbCursor.execute(f"SELECT * FROM songs WHERE songID = {songID}")

        # The fetchone method fetches a unique method
        row = dbCursor.fetchone()

        # None is a singleton object that checks if a value is present
        if row == None:
            print(f"No record with the SongID {songID} exists")
        else:
            fieldName = input("Enter the (Title or Artist or Genre): ").title()
            fieldValue = input(f"Enter the value for {fieldName}: ")

            # UPDATE songs SET Title or Artist or Genre = TitleValue or ArtistValue or GenreValue WHERE SongID = 1/2/3/4/5...
            dbCursor.execute(f"UPDATE songs SET {fieldName} = ? WHERE songID = ? ", (fieldValue, songID))
            dbCon.commit()
            print(f"Record with SongID {songID} updated")
    
    except sql.OperationalError as e:
        print(f"Failed because : {e}")
    except sql.ProgrammingError as pe:
        print(f"Failed because of Programming Error: {pe}")
    except sql.Error as er:
        print(f"Failed because Error: {er}")
if __name__ == "__main__":
    update_song()