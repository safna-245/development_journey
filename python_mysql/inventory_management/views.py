from mysql import connector

class InventoryCreateListRetrieveUpdateDelete:

    def __init__(self,user=None,password=None):

        if user==None or password==None:

            raise Exception("username and password required")

        self.connection = connector.connect(
            user=user,
            password=password,
            host="localhost",
            database="inventory_db"
        )

        self.cursor = self.connection.cursor()

    def post(self,**kwargs):
            
            db_cols = ("item_name","sku","category","quantity","reorder_level","unit_price","storage_zone","status")
    
            difference= set(db_cols).difference(kwargs.keys())
    
            if difference:
    
                raise Exception(f"{difference} required")
    
            col_str=",".join(db_cols)
    
            query=f""" insert into inventory ({col_str}) values(%s,%s,%s,%s,%s,%s,%s,%s)"""
    
            values = list(kwargs.values())
    
            self.cursor.execute(query,values)
    
            self.connection.commit()
    
            print("inventory has been added...")

    def get(self):
    
            query="select * from inventory"
    
            self.cursor.execute(query)
    
            records = self.cursor.fetchall()
    
            for i in records:
    
                print(i)

    def retrieve(self,item_id =None):
            
            query="select * from inventory where item_id =%s"
    
            values=(item_id,)
    
            self.cursor.execute(query,values)
    
            record = self.cursor.fetchone()
    
            print(record)

    def delete(self,**kwargs):

        place_holder=""
                
        for k in kwargs.keys():

            place_holder += k+"=%s,"

        place_holder= place_holder.rstrip(",")
        
        query=f"delete from inventory where {place_holder}"
        
        values=list(kwargs.values())
        
        self.cursor.execute(query,values)
        
        self.connection.commit()

        print("record deleted...")

    def put(self,item_id =None,**kwargs):
        
                place_holder=""
        
                for k in kwargs.keys():
        
                    place_holder += k+"=%s,"
        
                place_holder= place_holder.rstrip(",")
        
                query=f"""update inventory  set {place_holder} where item_id =%s"""
        
                values= list(kwargs.values())
        
                values.append(item_id )
        
                self.cursor.execute(query,values)
        
                self.connection.commit()
        
                print("record updated.. ")

    def filter(self,**kwargs):
    
            place_holder = ""
    
            for k in kwargs.keys():
    
                place_holder +=k+"= %s and "
    
            place_holder = place_holder.rstrip("and ")
    
            query=f"select * from inventory where {place_holder}"
    
            values = list(kwargs.values())
    
            self.cursor.execute(query,values)
    
            records = self.cursor.fetchall()
    
            if records:
    
                for i in records:
    
                    print(i)
    
            else:
    
                print("No records...")

    def summary(self):
    
            query= "select  item_name,sum(quantity * unit_price) as total_inventory from inventory group by item_name"
    
            self.cursor.execute(query)
    
            inventary_statistics = self.cursor.fetchall()
    
            category_summary_query = "select category,count(*) as count from inventory group by category"
    
            self.cursor.execute(category_summary_query)
    
            category_summary = self.cursor.fetchall()
    
    
            print("category summary",category_summary)
    
            print("inventary_statistics",inventary_statistics)
    
    

inventory = InventoryCreateListRetrieveUpdateDelete(user="root",password="Password@123")

#print(inventory.connection)

#inventory.post(item_name="Office Table",sku="OT001",category="Furniture",quantity=0,reorder_level=5,unit_price=5500.00,storage_zone="Zone-B",status="Out of stock")

#inventory.get()

#inventory.retrieve(item_id=2)

#inventory.put(quantity=30,unit_price=800.00,item_id=1)

#inventory.delete(status="Discontinued")

#inventory.filter(category="Electronics")


#inventory.summary()

#inventory.put(storage_zone="Zone-A",item_id=2)


