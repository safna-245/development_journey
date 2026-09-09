"""
Employee id,name,salary,phone,department
        -setemployee(id,name,salary,phone,department)
        -getemployee()
"""

class Employee:

    id:int
    name:str
    salary:int
    phone:int
    department:str

    def __init__(self,id,name,salary,phone,department):

        self.id = id
        self.name = name
        self.salary = salary
        self.phone = phone
        self.department = department

    def get_Employee(self):

        print(self.id,self.name,self.salary,self.phone,self.department)
emp1_instance = Employee(10,"Manu",50000,9823145678,"HR")
10,"Manu",50000
emp2_instance = Employee(15,"Rahul",30000,9923145678,"Sales")

emp1_instance.get_Employee()
emp2_instance.get_Employee()
       