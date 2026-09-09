def fibonacci(limit):

    first = 0

    second = 1

    
    for i in range(1,limit+1):

        next = first + second

        print(first)

        first = second

        second = next

fibonacci(10)
