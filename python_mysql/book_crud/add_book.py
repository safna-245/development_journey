from mysql import connector

connection = connector.connect(
    user="root",
    password="Password@123",
    host="localhost",
    database="book_db"
)

cursor = connection.cursor()

query = """
insert into book(title,price,pages,author) values(%s,%s,%s,%s);
"""

values = ("The fault in our stars",450.00,313,"John Green")

cursor.execute(query,values)

connection.commit()

connection.close()

print("record has been insered...")



