from mysql import connector

class TicketCreateListRetrieveUpdateDelete:

    def __init__(self,user=None,password=None):

        if user==None or password==None:

            raise Exception("username and password required")

        self.connection = connector.connect(
            user=user,
            password=password,
            host="localhost",
            database="customer_support_db"
        )

        self.cursor = self.connection.cursor()

    def post(self,**kwargs):
        db_cols = ("customer_name","email","subject","description","category","priority","status","assigned_to")

        difference= set(db_cols).difference(kwargs.keys())

        if difference:

            raise Exception(f"{difference} required")

        col_str=",".join(db_cols)

        query=f""" insert into support_ticket ({col_str}) values(%s,%s,%s,%s,%s,%s,%s,%s)"""

        values = list(kwargs.values())

        self.cursor.execute(query,values)

        self.connection.commit()

        print("ticket has been added...")

    def get(self):

        query="select * from support_ticket"

        self.cursor.execute(query)

        records = self.cursor.fetchall()

        for t in records:

            print(t)

    def retrieve(self,id=None):

        query="select * from support_ticket where id=%s"

        values=(id,)

        self.cursor.execute(query,values)

        record = self.cursor.fetchone()

        print(record)

    def put(self,id=None,**kwargs):
    
            place_holder=""
    
            for k in kwargs.keys():
    
                place_holder += k+"=%s,"
    
            place_holder= place_holder.rstrip(",")
    
            query=f"""update support_ticket  set {place_holder} where id=%s"""
    
            values= list(kwargs.values())
    
            values.append(id)
    
            self.cursor.execute(query,values)
    
            self.connection.commit()
    
            print("record updated.. ")

    def filter(self,**kwargs):

        place_holder = ""

        for k in kwargs.keys():

            place_holder +=k+"= %s and "

        place_holder = place_holder.rstrip("and ")

        query=f"select * from support_ticket where {place_holder}"

        values = list(kwargs.values())

        self.cursor.execute(query,values)

        records = self.cursor.fetchall()

        if records:

            for t in records:

                print(t)

        else:

            print("No records...")

    def summary(self):

        query= "select status,count(*) as count from support_ticket group by status"

        self.cursor.execute(query)

        response = self.cursor.fetchall()

        priority_summary_query = "select priority,count(*) as count from support_ticket group by priority"

        self.cursor.execute(priority_summary_query)

        priority_summary = self.cursor.fetchall()


        print("priority summary",priority_summary)

        print(response)

 






ticket=TicketCreateListRetrieveUpdateDelete(user="root",password="Password@123")

#print(ticket.connection)

#ticket.post(customer_name="jibin",email="jibin@gmail.com",subject="payment deducted but order pending",description="i made the payment yesterday but my order is still showing pending",category="payment",priority="medium",status="colsed",assigned_to="Rahul")

#ticket.get()

#ticket.retrieve(id=1)

#ticket.put(id=1,assigned_to="jithin")

#ticket.filter(priority="high")

ticket.summary()


