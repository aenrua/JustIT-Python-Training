from connect import *

# create a subroutine to add songs to the songs table
def insert_song():
    try:
        # SongID is an auto increment field so no data is required
        
        # create variables for each field to store the respective data from the input function
        # SongID, Artist, Title, Genre
        sTitle = input("Enter song title: ")
        sArtist = input("Enter song artist: ")
        sGenre = input("Enter song genre: ")
        
        dbCursor.execute("INSERT INTO songs VALUES(NULL,?,?,?)", (sTitle, sArtist, sGenre))
        # dbCursor.execute("INSERT INTO songs (Title, Artist, Genre) VALUES(?,?,?)", (sTitle, sArtist, sGenre))
        dbCon.commit()
        print(f"{sTitle} inserted in the songs table")

    except sql.OperationalError as e:
        print(f"Failed because : {e}")
    except sql.ProgrammingError as pe:
        print(f"Failed because of Programming Error: {pe}")
    except sql.Error as er:
        print(f"Failed because Error: {er}")
if __name__ == "__main__":
    insert_song()