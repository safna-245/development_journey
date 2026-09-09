"""### 3. Heart Rate
- < 60: Low
- 60 â€“ 100: Normal
- > 100: High
"""
heart_rate = int(input("Enter heart rate:"))

if heart_rate < 60:
    
    print("Low")

elif heart_rate >= 60 and heart_rate <= 100:

    print("Normal")

else:

    print("High")

