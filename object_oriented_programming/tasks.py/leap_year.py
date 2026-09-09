class LeapYear:

    def solution(self,year):

        if (year%100==0 and year%400==0) or (year%100 != 0 and year%4 ==0):

            return True
        
        else:

            return False

year_instance = LeapYear()

print(year_instance.solution(2014))

print(year_instance.solution(2000))
