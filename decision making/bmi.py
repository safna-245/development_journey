height_in_cm=int(input("Enter your height:"))

weight_in_kg=int(input("Enter your weight:"))

height_in_meter=height_in_cm/100

bmi=weight_in_kg/height_in_meter**2

print(bmi)

if bmi<=19:print("Under weight")

elif bmi>19 and bmi<=25:print("Normal")

elif bmi>25 and bmi>=30:print("over weight")

else:print("obese")