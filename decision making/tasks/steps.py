"""7. Daily Steps
- < 5000: Sedentary
- 5000 â€“ 9999: Moderately Active
- â‰¥ 10000: Active

"""
steps = int(input("Enter steps duration:"))

if steps < 5000:
    
    print("sedentary")

elif steps >=5000  and steps <=9999:

    print("Moderately active")

else:

    print("Active")
