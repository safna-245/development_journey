sales = [100000,120000,110000,115000,100000,116000]
#display march month sales

march_month_sale = sales[0]

print(march_month_sale)

print("may month sales updated...")
sales[4] = 105000

print(sales)

print("display all sales using index")
for i in range(0,len(sales)):

    print(sales[i])

print("display sales >100000")

for sale in sales:

    if sale > 100000:

        print(sale)



