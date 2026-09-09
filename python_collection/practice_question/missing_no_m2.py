"""
step : sort array

step2: repeat for p from 0 to length of arr -1

step3: set c as p+1

step4:set difference = arr[c]- arr[p]

step5:check if difference != 1 then dispaly missing as arr[p]+1 and exit


"""


arr = [1,3,4,5,6]

arr.sort()

for p in range(0,len(arr)-1):

    c= p + 1

    difference = arr[c] - arr[p]

    if difference != 1:

        print(arr[p]+1,"is missing")

        break