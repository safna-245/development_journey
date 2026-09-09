def last_divisor(number):

    
    for i in range(1,number):
        
        if(number%i == 0):
            
            gcd = i
        
    print(gcd)

last_divisor(6)

last_divisor(8)