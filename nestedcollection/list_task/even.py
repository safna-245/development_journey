#Find all even numbers in a list.
lst = [2,1,3,5,6,8,12,16,13]

even = [num for num in lst if num%2 == 0]

print(even)