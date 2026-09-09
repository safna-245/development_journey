x1 = int(input("Enter x1:"))

y1 = int(input("Enter y1:"))

x2 = int(input("Enter x2:"))

y2 = int(input("Enter y2:"))

x3 = int(input("Enter x3:"))

y3 = int(input("Enter y3:"))

slope1 = (y2-y1)/(x2-x1)

slope2 = (y3-y2)/(x3-x2)

if slope1 == slope2:

    print("points can form a straight line")

else:

    print("points can't form a straight  line")
