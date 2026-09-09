arr = [10,1,15,16,11,10,12,11,12,18,12]

most_frequent = arr[0]

max_count = arr.count(arr[0])

for num in arr:

    if arr.count(num) > max_count:

        most_frequent = num

print(most_frequent)





    

