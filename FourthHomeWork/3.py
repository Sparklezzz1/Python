import random

class BankAccount:

    def __init__(self,__balance,__account_number):
        self.__balance = __balance
        self.__account_number = __account_number

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Баланс меньше 0")
        self.__balance = value 
   
    @property
    def account_number(self):
        return self.__account_number
    

    @staticmethod
    def generate_account_number():
        return random.randrange(10**9, 10**10)
    
    @classmethod
    def create_account(cls, initial_balance):
        cls.initial_balance = initial_balance
        account_num = cls.generate_account_number()
        return cls(initial_balance, account_num)
    
account = BankAccount.create_account(1000)
print(account.balance)          
account.balance = -500