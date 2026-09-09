words = ["madam","ant","net","malayalam","english"]

palindrome_words = []

for w in words:

    reversed = w[::-1]

    if w == reversed:

        palindrome_words.append(w)

print(palindrome_words)