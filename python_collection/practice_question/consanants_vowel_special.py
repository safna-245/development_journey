text = "$hello#world!!"

vowel = []

consonants = []

special = []

for ch in text:

    if ch.lower() in "aeiou":

        vowel.append(ch)

    elif ch.isalpha():

        consonants.append(ch)

    else:

        special.append(ch)

print("Vowels=",vowel)

print("Consonants=",consonants)

print("Special character =",special)