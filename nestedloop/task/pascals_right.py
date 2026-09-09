for r in range(1,5):

    for c in range(1,8):

        if r <= 8:
            if (c <= 2*r-1 and c%2 != 0):
                
                print("*",end=" ")

            else:

                print(" ",end=" ")

            
    
        else:
            
            if c>=2*(2*r-4)+1 and  c<= 2*4-1 and c%2 != 0:
                
                print(" ",end=" ")

            else:

                 print(" ",end=" ")




    print()
         
         
