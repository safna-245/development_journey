employee = {"id":12,"name":"shyam","dept":"hr"}

key = input("enter key:")

try:

    print(employee[key])

except Exception as e:

    print(e)

finally:

    print("db commit..")