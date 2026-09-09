expenses = [12000,15000,13000,14000,11000]

march_month_expense = expenses[2]

print(march_month_expense)

expenses[3] = 11500

print(expenses)

#iterate through list
#display one by one

print("using index---")

for i in range(0,len(expenses)):

    print(expenses[i])


print("using in ----")


for amount in expenses:

    print(amount)