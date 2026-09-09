#first missing number in array
arr = [1,2,4,5]

"""
for num in range(1,len(arr)+2):

    if num not in arr:

        print(num)
        break
        
"""

"""
step1: set max_num  as largest number of arr

step2: set total as sum of numbers form 1 ro max_num

step3:set current_sum as sum ofnnumbers in  arr

step4: set difference as total - current_sum


"""

max_num =  max(arr)

total = 0

for num in range(1,max_num+1):

    total = total + num

current_arr_sum = sum(arr)

difference = total - current_arr_sum

print(difference)
    

