from connect import *

def search_song():
    try:
        # dbCursor.execute("SELECT * FROM songs ORDER BY Title DESC")
        # dbCursor.execute("SELECT * FROM songs WHERE Genre = 'Pop' ")
        dbCursor.execute("SELECT * FROM songs ORDER BY SongID ASC")

        allSongs = dbCursor.fetchall()
        for songs in allSongs:
            print(songs)
    
    except sql.OperationalError as e:
        print(f"Failed because : {e}")
    except sql.ProgrammingError as pe:
        print(f"Failed because of Programming Error: {pe}")
    except sql.Error as er:
        print(f"Failed because Error: {er}")
if __name__ == "__main__":
    search_song()