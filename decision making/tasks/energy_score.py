
energy_score = int(input("Enter energy score(1-10):"))

if energy_score >= 1 and energy_score <= 3:

    print("Low")

elif energy_score > 5  and energy_score <= 7:

    print("Moderate")

elif energy_score > 8 and energy_score <= 10:

    print("High")

else:
    print("Invalid ")
    
