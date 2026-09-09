"""john18
alice22
bob 16
emma 25"""

lst = [
    ("john",18),
    ("alice",22),
    ("Bob",16),
    ("emma",25)]

result = [i[0]  for i in lst if i[1] >= 18]

print(result)