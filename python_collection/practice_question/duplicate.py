arr = [10,1,15,16,11,10,12,11]

duplicate = set()

for  num in arr:

    length = arr.count(num)

    if length > 1 :

        duplicate.add(num)

print(duplicate)

