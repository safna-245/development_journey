# import connector from mysql

from mysql import connector

#create connection object

connection = connector.connect(
    user="root",
    password="Password@123",
    host="localhost",
    database="song_db"
)

#create cursor object
cursor= connection.cursor()
#set query
query="""
    insert into song(title,track_number,movie,singers) values(%s,%s,%s,%s);
"""

values=("Pavizha mazha",3,"athiran","K.S Harisankar")

cursor.execute(query,values)

connection.commit()

connection.close()

print("record has been inserted..")

