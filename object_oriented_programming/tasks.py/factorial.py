class Factorial:

    def solution(self,num):

        result = 1

        for i in range(1,num+1):

            result *= i

        return result

num_instance = Factorial()

print(num_instance.solution(5))

print(num_instance.solution(4))