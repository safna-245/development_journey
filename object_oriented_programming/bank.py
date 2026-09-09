class Bank():

    acc_number:int
    balance:float
    act_type:str
    customer_name:str

    def __init__(self,acc_number,balance,act_type,customer_name):

        self.acc_number = acc_number

        self.balance = balance

        self.act_type = act_type

        self.customer_name = customer_name

        print("account has been created")

    def deposit(self,amount):

        self.balance += amount

        print(f"your {self.acc_number} has been credited with ({amount} available balance {self.balance})")

    def withdraw(self,amount):

        if self.balance < amount:

            raise Exception("insufficient balance...")  

        else:

            self.balance -= amount

            print(f"your {self.acc_number} has been credited with ({amount} available balance {self.balance})")

    def get_balance(self):

        print("your available balance is ",self.balance)

bank_instance_1= Bank(12345,2000,"saving","jhon")

bank_instance_1.withdraw(1000)

bank_instance_1.deposit(20000)

bank_instance_1.get_balance()



