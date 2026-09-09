words = ["silent","listen","race","care","trap","night","tight"]

fw = open("file_operation\\anagrams.txt","w")

for w1 in words:

    for w2 in words:

        if sorted(w1) == sorted(w2) and w1 != w2:

            fw.write(w1 +"\n")

    
print("completed...")

fw.close()
            

    