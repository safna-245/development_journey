num = int(input("enter number to find factorial--"))
fact = 1
i = 1

while( i<= num):

    fact = fact * i
    
    i = i+1


print("Factorial=",fact)