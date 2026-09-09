class Superhero:

    name:str
    power:str
    universe:str

    def __init__(self,name,power,universe):

        self.name = name

        self.power = power

        self.universe = universe

    def get_superhero(self):

        print(self.name,self.power,self.universe)

super_hero_instance1 = Superhero("Spyderman","spreadweb","marvel")

super_hero_instance2 = Superhero("Batman","rich","dc")

super_hero_instance3 = Superhero("Minnal murali","run","basil")

super_hero_instance1.get_superhero()

super_hero_instance2.get_superhero()

super_hero_instance3.get_superhero()

"""
initialize attributes ->constructor

name of constructor will be __init__

do not need to call sepertely 
automatically call when object is created

"""