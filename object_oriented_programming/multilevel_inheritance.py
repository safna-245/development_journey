class GrandParent:

    def properties(self):

        print("2 acre land....")

class Parent(GrandParent):

    def home(self):

        print("1500 sqft house..")


class Child(Parent):

    def social_media(self):

        print("social media account")


child_instance = Child()

child_instance.social_media()

child_instance.home()