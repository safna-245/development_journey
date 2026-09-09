"""
polymorphism

more than one form or many form

method_over_loading- same method name ,different parameter(last write method only consider python)

method overriding

"""
#method overloading
class Calculator:

    def add(self,num1,num2):

        print(num1 +num2)

    def add(self,num1,num2,num3):
    
            print(num1 +num2+num3)
    
    def add(self,num1,num2,num3,num4):
    
            print(num1 +num2+num3+num4)

cacl_instance = Calculator()

cacl_instance.add(12,20,8,9)

    

