arr = [10,1,15,16,17,10,1]

arr_set = set(arr)

num_count = {}

for num in arr_set:

    num_count[num] = arr.count(num)

print(num_count)