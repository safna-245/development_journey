"""2. Blood Pressure (Systolic)
- < 120: Normal
- 120 â€“ 129: Elevated
- 130 â€“ 139: High BP Stage 1
- â‰¥ 140: High BP Stage 2

"""
blood_pressure = int(input("Enter blood pressure:"))

if blood_pressure < 120:
    
    print("Normal")

elif blood_pressure >= 120 and blood_pressure <= 129:

    print("Elevated")

elif blood_pressure >= 130 and blood_pressure <= 139:

    print("High BP Stage 1")

else:

    print("High BP Stage 2")
