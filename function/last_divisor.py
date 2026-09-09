number = int(input("Enter the number:"))

gcd = 1

for i in range(1,number):

    if(number%i == 0):

        gcd = i
        

print(gcd)

