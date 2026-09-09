class Parent:

    def properties(self):

        print("2 Kg golad,2 car")

    def groom(self):

        print("gopalan")

class Child(Parent):

    def groom(self):

        print("asif..")

child_instance = Child()

child_instance.properties()

child_instance.groom()