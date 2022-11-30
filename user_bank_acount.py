class Checking:
    def __init__(self, amount):
        self.balance = amount

    def display_account(self):
        print(f"Bank account balance: {self.balance}")

    def make_deposit(self, deposit):
        self.balance = self.balance + deposit

    def make_withdraw(self, withdraw):
        self.balance = self.balance - withdraw

class Person:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
        self.account = Checking(450)

    def deposit(self, amount):
        self.account.make_deposit(amount)

    def withdraw(self, withdrawn):
        self.account.make_withdraw(withdrawn)

    def display_info(self):
        print("------")
        print(f"First Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Current City: {self.location}")
        print(f"Bank Account Balance: {self.account}")

        


Jackie = Person("Jackie", 99, "The Moon")

Jackie.display_info()