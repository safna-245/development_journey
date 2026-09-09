""" **Exercise (Min)**: < 30 (Insufficient), 30 â€“ 60 (Good), > 60 (Intense)
"""
excercise_time = int(input("Enter Excercise time in minutes :"))

if excercise_time < 30:

    print("Insufficient")

elif excercise_time > 30 and excercise_time <= 60:

    print("Good")

else:
    
    print("Intense")
