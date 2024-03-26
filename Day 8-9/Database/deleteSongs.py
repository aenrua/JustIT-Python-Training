from connect import *

def delete_song():
    try:
        # SongID is primary key field
        songID = int(input("Enter the SongID of the record to be deleted: "))
        dbCursor.execute(f"SELECT * FROM songs WHERE SongID = {songID}")

        # The fetchone method is a unique (one) record
        row = dbCursor.fetchone()

        if row == None:
            print(f"Delete is not possible as no record with the SongID {songID} exists!")
        else:
            dbCursor.execute("DELETE FROM songs WHERE songID = ?", (songID,))
            dbCon.commit()
            print(f"The record {songID} deleted from the songs table")

    except sql.OperationalError as e:
        print(f"Failed because : {e}")
    except sql.ProgrammingError as pe:
        print(f"Failed because of Programming Error: {pe}")
    except sql.Error as er:
        print(f"Failed because Error: {er}")
if __name__ == "__main__":
    delete_song()