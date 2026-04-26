class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.isValidAccount(account1) and self.isValidAccount(account2):
            if self.withdraw(account1, money): 
                self.deposit(account2, money)
                return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if self.isValidAccount(account): 
            self.balance[account-1] += money
            return True 
        return False
        
    def withdraw(self, account: int, money: int) -> bool:
        if self.isValidAccount(account) and self.balance[account-1] >= money: 
            self.balance[account-1] -= money
            return True 
        return False

    def isValidAccount(self, account):
        return 1 <= account <= len(self.balance)