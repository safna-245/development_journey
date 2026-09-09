def is_palindrome(word):

    if word == word[::-1]:

        result = True

        return result

    else:

        result = False

        return result


assert is_palindrome("dad") == True,"test case 1 failed"
assert is_palindrome("tan") == False,"test case 2 failed"
assert is_palindrome("malayalam") == True,"test case 3 failed"