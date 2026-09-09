class FundWise:

    def __init__(self):

        self.fundwise = [
            {"id":1,"title":"Bus Ticket","amount":50,"category":"Travel","owner":"Anu"}
        ]

    def post(self,**kwargs):

        required_fields = {"id","title","amount","category","owner"}
                      
        missing_fields = required_fields.difference(kwargs.keys())

        if missing_fields:

            raise ValueError(missing_fields,"missing")

        self.fundwise.append(kwargs)

        print("Fund has been added")

    def get(self):

        print(self.fundwise)   

fundwise_instance = FundWise()

fundwise_instance.post(id=2,title="Groceries",amount=1000,category="shopping",owner="Manu")

fundwise_instance.get()
