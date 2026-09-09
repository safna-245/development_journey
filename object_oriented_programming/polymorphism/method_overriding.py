"""
methodoverriding:(same method name ,different class name,same no of parameters)

child class redefine the method that is already defined in parent class

"""
class Parent:

    def mobile(self):

        print("redmi note 14")

class Child(Parent):

    def mobile(self):

        print("one plus")

child_instance = Child()

child_instance.mobile()
