class Palindrome:

    def solution(self,word):

        result = True

        left = 0

        right = len(word)-1

        while(left<right):

            if word[left] != word[right]:

                result=False
                break
            
            left = left +1

            right = right - 1

        print(word)

        return result

pal_instance = Palindrome()

print(pal_instance.solution("hello"))

print(pal_instance.solution("madam"))