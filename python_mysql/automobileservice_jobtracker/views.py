from mysql import connector

class AutoserviceCreateRetrieveUpdateDelete:

    def __init__(self,user=None,password=None):
    
            if user==None or password==None:
    
                raise Exception("username and password required")
    
            self.connection = connector.connect(
                user=user,
                password=password,
                host="localhost",
                database="auto_service_db"
            )
    
            self.cursor = self.connection.cursor()

    def post(self,**kwargs):

         db_cols = ("customer_name","vehicle_number","vehicle_model","issue_description" ,"assigned_mechanic" ,"status" ,"estimated_cost","final_bill")

         difference = set(db_cols).difference(kwargs.keys())

         if difference:

              raise Exception(f"{difference} required")

         col_str=",".join(db_cols)

         query=f""" insert into job_cards ({col_str}) values(%s,%s,%s,%s,%s,%s,%s,%s)"""

         values = list(kwargs.values())

         self.cursor.execute(query,values)
             
         self.connection.commit()
             
         print("vehicle has been added...")

    def get(self):
    
        query="select * from job_cards"
        
        self.cursor.execute(query)
        
        records = self.cursor.fetchall()

        for i in records:

                print(i)

    def retrieve(self,job_id=None):

        query="select * from job_cards where job_id =%s"
        
        values=(job_id ,)
        
        self.cursor.execute(query,values)
        
        record = self.cursor.fetchone()
        
        print(record)

    def put(self,job_id =None,**kwargs):
            
        place_holder=""

        for k in kwargs.keys():

            place_holder += k+"=%s,"

        place_holder= place_holder.rstrip(",")

        query=f"""update job_cards set {place_holder} where job_id =%s"""

        values= list(kwargs.values())

        values.append(job_id )

        self.cursor.execute(query,values)

        self.connection.commit()

        print("record updated.. ")

    def delete(self,**kwargs):
    
            place_holder=""
                    
            for k in kwargs.keys():
    
                place_holder += k+"=%s,"
    
            place_holder= place_holder.rstrip(",")
            
            query=f"delete from job_cards where {place_holder}"
            
            values=list(kwargs.values())
            
            self.cursor.execute(query,values)
            
            self.connection.commit()
    
            print("record deleted...")

    def filter(self,**kwargs):
        
        place_holder = ""

        for k in kwargs.keys():

            place_holder +=k+"= %s and "

        place_holder = place_holder.rstrip("and ")

        query=f"select * from job_cards where {place_holder}"

        values = list(kwargs.values())

        self.cursor.execute(query,values)

        records = self.cursor.fetchall()

        if records:

            for v in records:

                print(v)

        else:

            print("No records...")
    
    def summary(self):
        
         query = """Select sum(final_bill) as total  from job_cards where status = 'Delivered'"""
         self.cursor.execute(query)

         job_statistics = self.cursor.fetchall()


         print("Total revenue",job_statistics)

    
    
    
    
    

vehicle = AutoserviceCreateRetrieveUpdateDelete(user="root",password="Password@123")

#print(vehicle.connection)

#vehicle.post(customer_name="Raju",vehicle_number="KL12AC1234",vehicle_model="Toyota Innova",issue_description="Oil Leakage",assigned_mechanic="Arun",status="Cancelled",estimated_cost=2000,final_bill=2800)

#vehicle.get()

#vehicle.retrieve(job_id =3)

#vehicle.putstatus=()"Ready for Pickup",job_id=3)

#vehicle.delete(job_id=4)

#vehicle.filter(assigned_mechanic="Ramesh")

#vehicle.summary()