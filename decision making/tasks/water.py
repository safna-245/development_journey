"""**Water Intake (Liters)**: < 2 (Dehydrated), 2 â€“ 3 (Adequate), > 3 (Excess)"""
water_intake = float(input("Enter water intake in liters:"))

if water_intake <= 2:
    print("Dehydrated")
elif water_intake > 2 and water_intake <= 3:
    print("Adequate")
else:
    print("Excess")