from connect import *

def read_songs():
    try:
        allSongs = dbCursor.execute("SELECT * FROM songs").fetchall()
        # dbCursor.execute("SELECT * FROM songs")
        # allSongs = dbCursor.fetchall()
        if allSongs:
            # format output
            "index    0       1                                 2                                3"
            print("SongID  | Title                          | Artist                         | Genre")
            print("*" * 60)

            for aSong in allSongs:
                print(f"{aSong[0]:7} | {aSong[1]:30} | {aSong[2]:30} | {aSong[3]:20}")
        else:
            print("No song found in the songs table")
    
    except sql.OperationalError as e:
        print(f"Failed because : {e}")
    except sql.ProgrammingError as pe:
        print(f"Failed because of Programming Error: {pe}")
    except sql.Error as er:
        print(f"Failed because Error: {er}")
if __name__ == "__main__":
    read_songs()