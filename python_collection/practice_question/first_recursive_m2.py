text = "ABCBADC"

char_count = {}

for ch in text:

    if ch in char_count:

        print(ch,"is the first recursive character")

        break

    else:

        char_count[ch] = 1
