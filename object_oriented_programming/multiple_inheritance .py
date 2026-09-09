class Father:

    def cricket_skill(self):

        print("father cricket skill")


class Mother:

    def dancing_skill(self):

        print("mother dancing skill")

class Child(Father,Mother):

    def coding_skill(self):

        print("Child coding skill")

child_instance = Child()

child_instance.coding_skill()

child_instance.dancing_skill()

child_instance.cricket_skill()