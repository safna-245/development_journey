angle1 = int(input("Enter angle1:"))

angle2 = int(input("Enter angle2:"))

angle3 = int(input("Enter angle3:"))

if angle1>0 and angle2>0 and angle3>0:

    if angle1+angle2+angle3 == 180:

        print("Triangle formed")

    else:

        print("Traingle not formed")

else:

    print("Invalid angle")

