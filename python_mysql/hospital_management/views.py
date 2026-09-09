from mysql import connector

class PatientCreateRetrieveUpdateDelete:

    def __init__(self,user=None,password=None):
    
            if user==None or password==None:
    
                raise Exception("username and password required")
    
            self.connection = connector.connect(
                user=user,
                password=password,
                host="localhost",
                database="hospital_db"
            )
    
            self.cursor = self.connection.cursor()

    def post(self,**kwargs):

         db_cols = ("patient_name","phone_number","assigned_doctor","department" ,"appointment_date" ,"status" ,"consultation_fee")

         difference = set(db_cols).difference(kwargs.keys())

         if difference:

              raise Exception(f"{difference} required")

         col_str=",".join(db_cols)

         query=f""" insert into patients ({col_str}) values(%s,%s,%s,%s,%s,%s,%s)"""

         values = list(kwargs.values())

         self.cursor.execute(query,values)
             
         self.connection.commit()
             
         print("patient has been added...")

    def get(self):

        query="select * from patients"
        
        self.cursor.execute(query)
        
        records = self.cursor.fetchall()

        for i in records:

             print(i)

    def retrieve(self,patient_id=None):

        query="select * from patients where patient_id=%s"
        
        values=(patient_id,)
        
        self.cursor.execute(query,values)
        
        record = self.cursor.fetchone()
        
        print(record)

    def put(self,patient_id=None,**kwargs):
            
        place_holder=""

        for k in kwargs.keys():

            place_holder += k+"=%s,"

        place_holder= place_holder.rstrip(",")

        query=f"""update patients set {place_holder} where patient_id=%s"""

        values= list(kwargs.values())

        values.append(patient_id)

        self.cursor.execute(query,values)

        self.connection.commit()

        print("record updated.. ")

    def filter(self,**kwargs):
        
        place_holder = ""

        for k in kwargs.keys():

            place_holder +=k+"= %s and "

        place_holder = place_holder.rstrip("and ")

        query=f"select * from patients where {place_holder}"

        values = list(kwargs.values())

        self.cursor.execute(query,values)

        records = self.cursor.fetchall()

        if records:

            for p in records:

                print(p)

        else:

            print("No records...")

    def summary(self):
        
        query= "select assigned_doctor,sum(consultation_fee ) as count from patients group by assigned_doctor"

        self.cursor.execute(query)

        consulation_fee_summary= self.cursor.fetchall()

        doctor_summary = "select assigned_doctor,count(*) from patients group by assigned_doctor"

        self.cursor.execute(doctor_summary)

        records = self.cursor.fetchall()


        print("Doctor summary",records)

        print("consulatation_fee_summary",consulation_fee_summary)


    def delete(self,patient_id=None):
    
        query="delete from patients where patient_id=%s"
        
        values=(patient_id,)
        
        self.cursor.execute(query,values)
        
        self.connection.commit()

        print("record deleted...")
        
        
    

     
             
            


patient = PatientCreateRetrieveUpdateDelete(user="root",password="Password@123")

#print(patient.connection)

#patient.post(patient_name="Rahul",phone_number="9256125689",assigned_doctor="Dr.Alice",department="Cardiology",appointment_date="2026-05-01",status="pending",consultation_fee=350.00)

#patient.get()

#patient.retrieve(patient_id=2)

#patient.put(assigned_doctor="Dr.Bobin",patient_id=2)

#patient.filter(status="pending" ,department="Dermatology")

#patient.summary()

#patient.delete(patient_id=3)