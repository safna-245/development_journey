"""
     *
    * *
   *   *
  *     *
 *       *
* * * * * *


"""

for r in range(1,6):

    for c in range(1,10):

        if r+c == 6 or c-r == 4:
        
            print("*",end=" ")

        elif r==5 and c%2 != 0:

            print("*",end=" ")


        else:

            print(" ",end=" ")

                            
    print()