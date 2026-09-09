#find two numbers in array whose sum is 9
arr = [2,3,4,5,11]

target = 9

for n1 in arr:

    for n2 in arr:

        total = n1 +n2

        if total == target and n1 != n2:

            print(n1,n2)

            break