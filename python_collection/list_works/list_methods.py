"""
    LIST METHODS

add

append(object)-add object at end of the list
insert(index,object)-add object at specified index

remove

pop(index=-1): remove element at the specified index
remove(value):remove element using value

index(value) - returns index postion of first occurenece of value
count(value)-retuns frequency of value
reverse()-reverse list 
sort()-sort list in ascending order
sort(reverse=True)-sort list in descending order
copy()
"""
#append()
colors = ["red","green","blue","red","violet","purple"]

colors.append("white")

print(colors)
#insert()
colors.insert(2,"orange")

print(colors)
#pop()
colors.pop()

print(colors)

colors.pop(3)

print(colors)

#remove()

colors.remove("violet")

print(colors)

#index()
orange_position = colors.index("orange")

print(orange_position)

#count()

red_count = colors.count("red")

print(red_count)

#reverse()

colors.reverse()

print(colors)

#sort()

colors.sort()#sort list in ascending order

print(colors)

colors.sort(reverse=True)#sort list in descending order

print(colors)

#copy()

pl_fvt_food = ["egg","chicken","Tea"]

p2_fvt_food = pl_fvt_food.copy()

p2_fvt_food[0] = "biriyani"

print("p1",pl_fvt_food)

print("p2",p2_fvt_food)