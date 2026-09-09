class Palindrome:

    def solution(self,word):

        result = True

        left = 0

        right = len(word)-1

        word = list(word)

        while(left<right):

            word[left],word[right] = word[right],word[left]

            left = left +1

            right = right - 1

        print(word)





        return result

pal_instance = Palindrome()

print(pal_instance.solution("hello"))

print(pal_instance.solution("madam"))