"""
dictionary

define = {"name":"acer234","brand":"acer"}
mutable
duplicate key not allowed

methods:
keys():
values():
items():
get(key):to get values  








"""
daily_calories = {"mon":2100,"tue":2200,
                  "wed":1800,"thur":1900,
                  "fri":2000,"sat":2200,
                  "sun":2500
                  }

sat_calorie = daily_calories["sat"]

print(sat_calorie)

daily_calories["thur"] = 1500#if the key doesnt exist return error message

print(daily_calories)

print("=== All Keys === ")

for k in daily_calories.keys():

    print(k)

print("== all values ==")

for v in daily_calories.values():

    print(v)

print("==All keys and values===")

for k,v in daily_calories.items():

    print(k,v)

tue_calorie = daily_calories.get("tue")

print(tue_calorie)

total_calorie = daily_calories.get("total")# if the key doesnt exist return none

print(total_calorie)

#add new keyvalue pair
daily_calories["tot_calorie"] = sum(daily_calories.values())

print(daily_calories)
"""
add key value
total = 0

for v in daily_calories.values():

    total += v

daily_calories["tot"] = total

print(daily_calories)
"""