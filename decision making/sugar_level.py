sugar_level=int(input("Enter the sugar level:"))

if sugar_level>300:

    print("very high")

elif sugar_level>=140 and sugar_level<=220:

    print("High")

elif sugar_level>=90 and sugar_level<140:

    print("Normal")

elif sugar_level>=80 and sugar_level<90:

    print("Low")

else:
    
    print("very low")
