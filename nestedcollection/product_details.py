product_details = [
["tomato",25,25],
["potato",30,10],
["onion",50,20],
["ginger",30,5],
["pumkin",20,15]
]

print(product_details[-2][1])

print(product_details[0][1:])

for lst in product_details:

    print(lst[0])

all_item_name = [lst[0] for lst in product_details]

print(all_item_name)