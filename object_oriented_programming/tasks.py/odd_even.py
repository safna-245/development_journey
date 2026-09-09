class OddEven:

    def solution(self,num):

        if num%2 == 0:

            result = "even"

        else:

            result = "odd"

        return result

num_instance = OddEven()

print(num_instance.solution(101))

print(num_instance.solution(112))