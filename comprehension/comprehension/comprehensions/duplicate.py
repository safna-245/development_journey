arr = [10,11,1,10,11,2,3]

duplicates = {num for num in arr  if arr.count(num)>1}

print(duplicates)