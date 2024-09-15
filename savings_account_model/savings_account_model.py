import random

f = open("logs.txt","w")

class BankAccount:
    def __init__(self, account_id, initial_balance):
        self.account_id = account_id
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            f.write(f'Account ID: {self.account_id} deposited: {amount} current balance: {self.balance}\n')
        else:
            f.write(f"Account ID: {self.account_id} Invalid deposit amount: {amount}\n")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            f.write(f'Account ID: {self.account_id} withdrawn: {amount} current balance: {self.balance}\n')
            self.balance -= amount
        else:
            f.write(f"Account ID: {self.account_id} Invalid Transaction of amount {amount}\n")
    
    def __str__(self):
        return f"Account {self.account_id}: Balance ${self.balance:.2f}"

def generate_transactions(account, num_months):
    for _ in range(num_months):
        num_transactions = random.randint(1, 5)
        for _ in range(num_transactions):
            transaction_type = random.choice(['deposit', 'withdraw'])
            amount = round(random.uniform(10, 500), 2)
            if transaction_type == 'deposit':
                account.deposit(amount)
            elif transaction_type == 'withdraw':
                account.withdraw(amount)

def main():
    num_accounts = 100
    num_months = 12
    
    accounts = []
    
    for account_id in range(1, num_accounts + 1):
        initial_balance = round(random.uniform(100, 10000), 2)
        account = BankAccount(account_id, initial_balance)
        generate_transactions(account, num_months)
        accounts.append(account)
        
    accounts.sort(key=lambda acc: acc.balance)
    
    for account in accounts:
        print(account)

if __name__ == "__main__":
    main()

f.close()
