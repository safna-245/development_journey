lst = [18,22,35,28,15]

result = ["cold" if t < 20 else "hot" if t >30 else "warm" for t in lst]

print(result)