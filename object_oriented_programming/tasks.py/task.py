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

class LeapYear:

    def solution(self,year):

        if (year%100==0 and year%400==0) or (year%100 != 0 and year%4 ==0):

            return True
        
        else:

            return False

year_instance = LeapYear()

print(year_instance.solution(2014))

print(year_instance.solution(2000))

class Factorial:

    def solution(self,num):

        result = 1

        for i in range(1,num+1):

            result *= i

        return result

num_instance = Factorial()

print(num_instance.solution(5))

print(num_instance.solution(4))

class Gcd:

    def solution(self,num1,num2):

        gcd = 1
        
        for i in range(1,min(num1,num2)+1):

            if(num1 % i == 0 and num2 % i == 0):

                gcd = i

        return gcd

gcd_instance = Gcd()

print(gcd_instance.solution(12,24))

print(gcd_instance.solution(24,18))
