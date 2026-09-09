class Shapes:

    name: str
    def __init__(self,name):

        self.name = name

class Rectangle(Shapes):

    length : int
    width : int

    def __init__(self, name,length,width):

        super().__init__(name)

        self.length = length

        self.width = width

    def area(self):

        print("area of",self.name,"=",self.length*self.width)

class Square(Shapes):

    length :int

    def __init__(self,name,length):

        super().__init__(name)

        self.length = length

    def area(self):

        print("area of",self.name,"=",self.length ** 2)

class Circle(Shapes):

    radius : float

    def __init__(self,name,radius):

        super().__init__(name)

        self.radius = radius

    def area(self):

        print("area of",self.name,"=",3.14*self.radius*2)

class Parallelogram(Shapes):

    base :int

    height:int

    def __init__(self,name,base,height):

        super().__init__(name)

        self.base = base

        self.height = height

    def area(self):

        print("area of",self.name,"=",self.base * self.height)

class Trapezium(Shapes):

    base1: int
    base2: int
    height :int

    def __init__(self,name,base1,base2,height):

        super().__init__(name)

        self.base1 = base1

        self.base2 = base2

        self.height = height

    def area(self):

        print("area of",self.name,"=",((self.base1 + self.base2) * self.height)/2)

p_instance = Parallelogram("Parallelogram",12,45)

p_instance.area()

c_instance = Circle("circle",3)

c_instance.area()


square_instance = Square("square",3)

square_instance.area()


rectangle_instance = Rectangle("rectangle",12,24)

rectangle_instance.area()

t_instance = Trapezium("Trapezium",10,20,4)

t_instance.area()






        