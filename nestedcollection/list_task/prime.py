lst = [9,2,5,7,12,15]

prime = []

for num in lst:

    for i in range(2,num):

        if num%i ==0:

            break
    else:

        prime.append(num)

print(prime)