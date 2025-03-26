# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         # Encapsulated (private) attribute: balance
#         self.__balance = balance

#     def deposit(self, amount):
#         """Deposit money into the account."""
#         if amount > 0:
#             self.__balance += amount
#             print(f"{self.owner} deposited Rs. {amount}.")
#         else:
#             print("Invalid deposit amount.")

#     def withdraw(self, amount):
#         """Withdraw money from the account after validating sufficient balance."""
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"{self.owner} withdrew Rs. {amount}.")
#         else:
#             print("Invalid withdrawal amount or insufficient funds.")

#     def get_balance(self):
#         """Provide a controlled way to view the account balance."""
#         return self.__balance

# # Creating an instance of BankAccount
# account = BankAccount("Easwer", 1000)
# account.deposit(500)          # Deposits Rs. 500
# account.withdraw(300)         # Withdraws Rs. 300
# print("Current Balance:", account.get_balance())

# Trying to access the balance directly would fail:
# print(account.__balance)  # This would raise an AttributeError
##---------------------------------------------------------------------

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner           # Public attribute
        self.__balance = balance     # Private attribute, encapsulated (hidden)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"\n{self.owner} Deposited {amount}. New balance: Rs. {self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"\n{self.owner} Withdrew {amount}. New balance: Rs. {self.__balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        # Provides controlled access to the private balance
        return self.__balance

# Using the BankAccount class
account = BankAccount("Easwer", 1000)
account.deposit(500)         # Deposited 500. New balance: Rs. 1500
account.withdraw(300)        # Withdrew 300. New balance: Rs. 1200
print("\nCurrent Balance:", account.get_balance(),"\n")  # Current Balance: Rs. 1200

#Direct access to __balance is not allowed:
#print(account.__balance)   # This will raise an AttributeError
