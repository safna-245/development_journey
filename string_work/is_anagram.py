def is_anagram(word1,word2):

    for ch in word1:
        
        if ch  not in word2 or word1.count(ch)!= word2.count(ch):
            
            print(False)
            
            break

    else:
        
        print(True)

is_anagram("silent","listen")
is_anagram("save","vase")
is_anagram("silents","listen")