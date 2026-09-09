def calculator(*args,**kwargs):

    if kwargs.get("operation") == "+":

        return sum(args)

    elif kwargs.get("operation") == "*":

        product = 1

        for num in args:

            product = product *num 

        return product

print(calculator(10,20,4, operation = "+"))

print(calculator(10,20,4, operation = "*"))
        
             