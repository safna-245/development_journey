#find two numbers in array whose sum is 16

arr = [2,3,4,5,11]

target = 16

for n in arr:

    difference = target  - n

    if difference in arr and difference != n:

        print(n,difference)

        break