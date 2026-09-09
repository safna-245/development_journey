def product(*args):

    product = 1

    for num in args:

        product = product * num

    return product

print(product(10,20,30))

print(product(10,20))