""""
Tuple
immutable,ordered,duplicates_allowed

methods:
count(value) frequency of value
index(value) first occurence
"""
tp = (10,20,30,30)

print(tp)

print(type(tp))
#tp[1] = 15 // error tuple cant change or modify
print(tp.count(30))

print(tp.index(30))

#only one element value must be end with ,
tup = (10,)
print(type(tup))
