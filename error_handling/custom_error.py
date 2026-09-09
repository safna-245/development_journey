#custom errors 
age = int(input("enter age:"))

if age < 18:

    raise Exception("Invalid age")

else:

    print("Eligible for voting")