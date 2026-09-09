"""**Cholesterol**: < 200 (Desirable), 200 â€“ 239 (Borderline), â‰¥ 240 (High)
"""
cholestrol=int(input("Enter choloestrol:"))

if cholestrol <= 200:print("Desirable")

elif cholestrol > 200 and cholestrol <= 239:print("Borderline")

elif cholestrol > 240:print("High")