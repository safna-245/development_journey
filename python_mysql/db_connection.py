# pip install mysql-connector-python
#step1: import connector from mysql module
from mysql import connector

#step2 : establish a connecton

connection = connector.connect(
    user="root",
    password="Password@123",
    host="localhost"
)

print(connection)