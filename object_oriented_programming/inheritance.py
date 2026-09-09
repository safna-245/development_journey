class Parent:

    def house(self):

        print("parent class house method")

class Child(Parent):

    def social_media_account(self):

        print("child class  social media account")

Child_instance = Child()

Child_instance.social_media_account()

Child_instance.house()

