fr = open("file_operation\\news.txt","r",encoding="utf-8")

words = []

for line in fr:

    line =line.rstrip("\n")

    for w in line.split(" "):

        words.append(w)

print(words)

words_count = {w:words.count(w) for w in words}

print(words_count)

