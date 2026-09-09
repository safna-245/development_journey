from mysql import connector

class IssuesListCreateRetrieveUpdateDelete:

    def __init__(self,user=None,password=None):

        self.connection=connector.connect(
            user="root",
            password="Password@123",
            host="localhost",
            database="road_issue_db"
        )

        self.cursor=self.connection.cursor()

    def post(self,**kwargs):

        query="insert into issues(title,location,posted_by,status) values(%s,%s,%s,%s)"

        values=list(kwargs.values())

        self.cursor.execute(query,values)

        self.connection.commit()

        print("record has been added...")

    def get(self):
    
            query="select * from issues"
    
            self.cursor.execute(query)
    
            records=self.cursor.fetchall()
    
            for issue in records:
    
                print(issue)

    def retrieve(self,id=None):
    
            query="select * from issues where id=%s"
    
            values=(id,)
    
            self.cursor.execute(query,values)
    
            record= self.cursor.fetchone()
    
            print(record)

    def put(self,id=None,**kwargs):
    
            place_holder=""
    
            for k in kwargs.keys():
    
                place_holder += k+"=%s,"
    
            place_holder= place_holder.rstrip(",")
    
            query=f"""update issues set {place_holder} where id=%s"""
    
            values= list(kwargs.values())
    
            values.append(id)
    
            self.cursor.execute(query,values)
    
            self.connection.commit()
    
            print("record updated.. ")


issue_instance=IssuesListCreateRetrieveUpdateDelete(user="root",password="Password@123")

#issue_instance.post(title="Large pothole",location="Thrissur",posted_by="anu",status="unsolved")

#issue_instance.get()

#issue_instance.retrieve(id=1)

issue_instance.put(title="Blocked road",posted_by="manu",id=1)
    