#closest number to zero
"""
step1:set closeset as arr[0]

step2: repeat for each num in arr:

    step3: check if abs(num) < abs(closest):

          step4: update closest as num

    step5: check if abs(num) == abs(closest) and num > closest 

            step6: update closest as num

step 7: display closest
           


"""
arr = [-1,-3,-2,2,3,4,1]

closest = arr[0]

for num in arr:

    if abs(num) < abs(closest):

        closest = num

    elif abs(num) == abs(closest) and num > closest:

        closest = num

print(closest)

