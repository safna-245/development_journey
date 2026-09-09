arr = [2,3,5,6,4,7,8]

evens = [num for num in arr if num%2 ==0]

print(evens)

odds =  [num for num in arr if num%2 !=0]

print(odds)

num_gt_five = [num for num in arr if num > 5]

print(num_gt_five)
