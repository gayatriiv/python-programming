class BankAccount:
    def __init__(self, account_no, name, balance=0.0):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

  
    def withdrawal(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

   
    def bank_fees(self):
        fees = self.balance * 0.05
        self.balance -= fees
        print(f"Bank fees: {fees}. New balance: {self.balance}")
    
    
    def display(self):
        print(f"Account No: {self.account_no}")
        print(f"Holder Name: {self.name}")
        print(f"Balance: Rs :{self.balance}")

    def __del__(self):
        print("Account Closed")


account = BankAccount(617234, "Gayatri Vinod ", 1000000.0)

# Deposit money
account.deposit(50000)

# Withdraw money
account.withdrawal(20000)

# Apply bank fees
account.bank_fees()

# Display account details
account.display()

# Delete account
del account
