"""**Weather Conditions**:
   - Above 30: Hot
   - 20 to 30: Warm
   - Below 20: Cold"""
temparature = int(input("Enter temperature:"))

if temparature >30:

    print("Hot")

elif temparature >= 20 and temparature <= 30:

    print("Warm")

else:
    
    print("Cold")
