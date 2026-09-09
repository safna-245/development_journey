"""5. Sleep Duration
- < 6: Sleep Deprived
- 6 â€“ 8: Healthy Sleep
- > 8: Oversleeping"""
sleep_duration = int(input("Enter sleep duration:"))

if sleep_duration < 6:
    
    print("Sleep Deprived")

elif sleep_duration >=6  and sleep_duration <=8:

    print("Healthy sleep")

else:

    print("Oversleeping")
