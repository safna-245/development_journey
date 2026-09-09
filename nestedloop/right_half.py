print("right half")

def right_half():

    for r in range(5,1,-1):
        
        for s in range(1,r+1):
             
          for c in range(1,s):
                
                print("*",end="  ")

        print()

right_half()