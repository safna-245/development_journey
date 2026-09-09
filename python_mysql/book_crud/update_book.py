from mysql import connector

connection = connector.connect(
    user="root",
    password="Password@123",
    host="localhost",
    database="book_db"
)

cursor = connection.cursor()

query = """
update book set title=%s,author=%s where id=%s

"""
values=("Wings of fire","A P J Abdul kalam",2)

cursor.execute(query,values)

connection.commit()

print("recod has been updated...")