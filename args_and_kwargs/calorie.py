#deatil:retrieve
#remove:delete
#list|all:get
#add|create:post
#update:put

class DietLens:

    def __init__(self):

        self.foodlogs = [

            {"id":1,"name":"dosa","calorie":180,"owner":"hari"}

        ]

    def post(self,**kwargs):

        required_fields = {"id","name","calorie","owner"}

        missing_fields = required_fields.difference(kwargs.keys())

        if missing_fields:

            raise ValueError(missing_fields,"missing")

        self.foodlogs.append(kwargs)

        print("Food logs has been added")

    def get(self):

        if len(self.foodlogs) == 0:

            print("No records found...")

        else:

            for log in self.foodlogs:

                print(log)

    def retrieve(self,id=None):

        if not id:

            raise ValueError("id missing")

        else:

            return [log for log in self.foodlogs if log.get("id")==id]

    def put(self,id=None,**kwargs):

        log =[log for log in self.foodlogs if log.get("id")==id][0]#list of dictionary to dictionary

        log.update(kwargs)

        print("record has been updated...")

        print(log)

    def delete(self,id=None):

        log = [log for log in self.foodlogs if log.get("id")==id][0]

        self.foodlogs.remove(log)

        print("food log removed")

        self.get()




                

diet_instance = DietLens()

diet_instance.post(id=2,name="idly",calorie=150,owner="vipin")

#diet_instance.get()

diet_instance.post(id=3,name="chapati",calorie=190,owner="anu")

#diet_instance.get()

#print(diet_instance.retrieve(id=2))

#diet_instance.put(id=1,name="ghee roast",calorie=200)

diet_instance.delete(id=2)







