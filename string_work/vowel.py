text = "supErcalifragilisticexpialidocious"

vowel_count = 0

for ch in text:

    if ch.lower() in "aeiou":

        vowel_count+=1

print(vowel_count)
