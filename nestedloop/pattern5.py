"""
     * =>row=6 space=5 col=1
    * * =>row=5 space=4 col=2
   * * *
  * * * *
 * * * * *
* * * * * *
"""

def pattern():

    for r in range(6,0,-1):
           
           for s in range(1,r):
                    
                print(" ",end="")

           for c in range(1,(7-r)+1):
                
                print("*",end=" ")
                
           print()

pattern()