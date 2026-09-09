""" **Screen Time (Hours)**: < 2 (Healthy), 2 â€“ 5 (Moderate), > 5 (Excessive)
"""
screen_time = int(input("Enter screen time in hours:"))

if screen_time <= 2:

    print("Healthy")

elif screen_time > 2 and screen_time <= 5:

    print("Moderate")

else:
    
    print("Excessive")