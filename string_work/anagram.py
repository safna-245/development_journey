word1 = "silent"

word2 = "listen"


for ch in word1:

    if ch  not in word2 or word1.count(ch)!= word2.count(ch):
        
        print("not anagram")

        break

else:

    print("anagram")
