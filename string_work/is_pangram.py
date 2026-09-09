def is_pangram(text):

    alphabets = "abcdefghijklmnopqrstuvwxyz"
    
    for alpha in alphabets:
        
        if alpha not in text.lower():
            
            print(False)
            
            break

    else:
        
        print(True)


is_pangram("how vexingly quick dAft zebras jump")
