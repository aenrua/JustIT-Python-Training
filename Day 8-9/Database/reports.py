from connect import *

def search_song():
    try:
        # Search by SongID or Title or Artist or Genre
        field = input("Search by SongID or Title or Artist or Genre: ")

        if field == "SongID":
            # Search by SongID
            songID = int(input("Enter SongID: "))
            dbCursor.execute("SELECT * FROM songs WHERE songID = ?", (songID,))
            row = dbCursor.fetchone()

            if row == None:
                print(f"No record with the SongID {songID} provided exists in the table")
            else:
                print(row)
        elif field in ["Title", "Artist", "Genre"]:
            # Search by Title or Artist or Genre
            strInput = (input(f"Enter the value for the field {field}: "))

            dbCursor.execute(f"SELECT * FROM songs WHERE {field} LIKE '%{strInput}%' ")

            rows = dbCursor.fetchall() # return all records that match the strinput variable

            if not rows:
                print(f"No record(s) with field {field} matching {strInput}")
            else:
                # Display all matching records based on the field and strInput
                for records in rows:
                    print(records)
        else:
            # Where the field to search is not SongID, Title, Artist, Genre
            print(f"Search field {field} invalid!")
    
    except sql.OperationalError as e:
        print(f"Failed because : {e}")
    except sql.ProgrammingError as pe:
        print(f"Failed because of Programming Error: {pe}")
    except sql.Error as er:
        print(f"Failed because Error: {er}")
if __name__ == "__main__":
    search_song()