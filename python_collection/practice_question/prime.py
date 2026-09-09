arr = [3,7,4,9,10,11,13]

prime = []

for num in arr:

    for i in range(2,num):

        if num%i == 0:

            break

    else:

        prime.append(num)

print(prime)