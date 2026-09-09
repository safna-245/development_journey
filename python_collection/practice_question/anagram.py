words = ["silent","listen","act","cat","note","tone","hen","chicken"]

anagram_words = set()

for i in range(0,len(words)):

    for j in range(0,len(words)):

        w1 = words[i]
        
        w2 = words[j]

        if sorted(w1) == sorted(w2) and w1 != w2:

            anagram_words.add(w1)

            anagram_words.add(w2)

print(anagram_words)
    
        

        