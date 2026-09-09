
urine_color = int(input("Enter urine color(1-8):"))

if urine_color > 1 and urine_color <=3:

    print("well hydrated")

elif urine_color>3 and urine_color <= 6:

    print("Mild dehydartion")

elif urine_color>6 and urine_color <= 8:
    
    print("severe")

else:

    print("Invalid urine color")

