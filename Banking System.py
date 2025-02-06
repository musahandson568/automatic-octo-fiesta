#banking system
deposit_amount=int(23000)
withdraw_amount=int(5000)
balance=int(1000)
user_name=input("Enter a name :")
class BankAccount:
    def __init__(self,account_number,user_name,balance,deposit_amount,withdraw_amount):
        self.user_name=user_name           #(input({user_name}))
        self.account_number=account_number
        self.balance=balance
        self.deposit_amount=deposit_amount
        self.withdraw_amount=withdraw_amount
    def deposit(self,deposit_amount):
        self.deposit_amount+=deposit_amount
        user_name:str=(input("Enter a name :"))
        print(f"{user_name} Deposited {deposit_amount} is Successful.\nNew balance : {self.deposit_amount}")
    def withdraw(self,withdraw_amount):
        self.withdraw_amount-=withdraw_amount
        print(f"Withdrawal of {withdraw_amount} is Successsful.\nNew balance : {self.withdraw_amount} \nThank You!")
    def get_balance(self):
        return self.balance
account=BankAccount("12540001", "Handson Musa",1000,23000,5000 )
print(f"User name is :{user_name}")
print(f"Account Number :{account.account_number}")
print(f"Amount Deposited :{account.deposit_amount}")
print(f"Your withdrawal Amount :{account.withdraw_amount}")
print(f"Net Balance :{account.get_balance()}")
