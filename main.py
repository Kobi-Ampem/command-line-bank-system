
class Transaction:
    def __init__(self, amount, transaction_type):
        self.amount = amount
        self.transaction_type = transaction_type



class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(Transaction(amount, 'Deposit'))
            print(f"Deposit of ${amount} succesful. New Balanace is ${self.balance}\n") # Add the choice to use country's currency symbol
        else:
            print("Invalid deposit amoun\nt")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Transaction(amount, 'Withdrawal'))
            print(f"Withdrawal of ${amount} succesful. New balance is ${self.balance}\n")
        else:
            print(f"Invalid withdrawal amount or insufficient funds\n") # Specify which case it is

    def display_transaction(self):
        print("\nTransaction History: ")
        for transaction in self.transactions:
            print(f"${transaction.amount} {transaction.transaction_type}")

    def display_balance(self):
        print(f"\nCurrent Balace for account{self.account_number}: ${self.balance}")


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self, account_number, holder_name, initial_balance=0):
        if account_number not in self.accounts:
            new_account = Account(account_number, holder_name, initial_balance)
            self.accounts[account_number] = new_account
            print(f"Account created succesfully for {holder_name}. Account number is {account_number}\n")
        else:
            print("Accountwith the given number already exists.\n")

    def get_account(self, account_number):
        return self.accounts.get(account_number)


  
bank = Bank('Absa Bank')

# create account
afia_account = bank.create_account(111, "Afia", 2400)
cy_account = bank.create_account(461, "Cyprian")

# accessing account
afia_account = bank.get_account(111)
cy_account = bank.get_account(461)

# making transactions
afia_account.deposit(500)
afia_account.withdraw(200)

cy_account.withdraw(300)
cy_account.deposit(1000)

# displaying transaction history and balances
afia_account.display_transaction()
cy_account.display_balance()
