sugar_level = int(input("Enter sugar level:"))

if sugar_level < 100:
    
    print("Normal")

elif sugar_level >= 100 and sugar_level <= 125:

    print("prediabetes")

else:

    print("Diabetes")
