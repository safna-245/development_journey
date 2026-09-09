"""**Calories**: < 1500 (Low), 1500 â€“ 2500 (Balanced), > 2500 (Excess)"""
calorie = int(input("Enter calorie:"))

if calorie < 1500:
    
    print("Low") 

elif calorie >= 1500 and calorie <= 2500:

    print("Balanced")

else:
    
    print("Excess")
