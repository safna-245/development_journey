"""### 4. Oxygen Level (SpO2)
- â‰¥ 95: Normal
- 90 â€“ 94: Mild Concern
- < 90: Critical

"""
oxygen_level = int(input("Enter oxygen level(SpO2):"))

if oxygen_level >= 95:
    
    print("Normal")

elif oxygen_level >= 90 and oxygen_level <= 94:

    print("Mild concern")

else:

    print("Critical")
