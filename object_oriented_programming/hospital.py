class Hospital:

    hospital_id : int
    name : str
    location:str
    phone:str

    def __init__(self,hospital_id,name,location,phone):

        self.hospital_id = hospital_id
        self.name = name
        self.location = location
        self.phone = phone

    def get_hospital(self):

        print(self.hospital_id,self.name,self.location,self.phone)

h1_instance = Hospital(1,"jubile mission","Thrissur","04884-242510")

h2_instance = Hospital(2,"Baby memorial","Kozhikode","04884-262510")

h1_instance.get_hospital()

h2_instance.get_hospital()