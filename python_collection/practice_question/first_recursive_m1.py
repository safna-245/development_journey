"""
first recursive character (first repeated character in the text)


step1: set unique words as empty list

step2:repeat for each ch in text:
     step3:chk ch in unique_words then dispaly ch and exit
     step4:else add ch to unique_words

"""

text = "ABCBADC"

unique_words = []

for ch in text:

    if ch in unique_words:

        print(ch,"is the first recursive character")

        break

    else:

        unique_words.append(ch)