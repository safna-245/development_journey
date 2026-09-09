temp_in_celcius = float(input("Enter body temprature:"))

if temp_in_celcius <= 36:

    print("Low")

elif temp_in_celcius > 36 and temp_in_celcius <= 37.5:

    print("Normal")

else:
    print("Fever")


