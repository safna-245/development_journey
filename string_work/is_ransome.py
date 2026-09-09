def is_ransome_note(note,magazine):
    
    for ch in note:
        
        if ch not in magazine:
            
            print(False)

            break

    else:

            print(True)

is_ransome_note("hen","chicken")
is_ransome_note("hen","chikn")

