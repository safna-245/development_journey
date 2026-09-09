"""
q1)word="python programming is simple"
    write a program to print character count

"""
word="python programming is simple"

char_set = set(word)

char_count = {}

for ch in char_set:

    char_count[ch] = word.count(ch)

print(char_count)


