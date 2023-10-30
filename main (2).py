# Implement a class called BankAccount that represents a bank account. The class should have private attributes for account number, account holder name, and account balance. Include methods to deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the BankAccount class and test the deposit and withdrawal functionality. 
class BankAccount:
    def __init__(self, account_number, account_holder_name, account_balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_balance = account_balance
      
    def deposit(self, amount):
        self.account_balance += amount
      
    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient balance")
        else:
            self.account_balance -= amount
          
    def display_balance(self):
        print(f"Account balance: {self.account_balance}")
      
account = BankAccount(1234, "John Doe", 500)
account.deposit(1000)
account.withdraw(500)
account.display_balance()