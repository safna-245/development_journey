text = "pneumonoultramicroscopicsilicovolcanoconiosis"

vowel_count = 0

consanant_count = 0

for ch in text:

    if ch.lower() in "aeiou":

        vowel_count+=1

    elif ch.isalpha():

        consanant_count+=1

print(vowel_count)

print(consanant_count)