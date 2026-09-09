arr = [10,1,15,16,11,10,12,11]

unique = []


for  num in arr:

    length = arr.count(num)

    if length == 1:

        unique.append(num)

print(unique)