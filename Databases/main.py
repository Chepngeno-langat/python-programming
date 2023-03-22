import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
#cur.execute("CREATE TABLE movie(title, year, score)")
# res = cur.execute("SELECT name FROM sqlite_master")
#cur.execute("INSERT INTO movie VALUES('Game Of Thrones', 2011, 9.0)")
# cur.execute("""
#     INSERT INTO movie VALUES
#         ('Monty Python and the Holy Grail', 1975, 8.2),
#         ('And Now for Something Completely Different', 1971, 7.5)
# """)

#cur.execute("CREATE TABLE music(id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, artist varchar(250) NOT NULL)")
# con.execute("INSERT INTO music VALUES(1, 'Would That I', 'Hozier')")
con.execute("INSERT INTO music VALUES(4, 'Riptide', 'Vance Joy')")
con.commit()
