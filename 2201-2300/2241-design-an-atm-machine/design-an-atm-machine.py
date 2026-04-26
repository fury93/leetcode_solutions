class ATM:

    def __init__(self):
        self.nominals = [20, 50, 100, 200, 500]
        self.bank = [0] * 5

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, count in enumerate(banknotesCount):
            self.bank[i] += count

    def withdraw(self, amount: int) -> List[int]:
        transaction = [0] * 5
        for count, nominal, i in zip(reversed(self.bank), reversed(self.nominals), range(4, -1, -1)):
            canTake = min(count, amount//nominal)
            transaction[i] = canTake
            amount -= canTake * nominal
        
        if amount == 0:
            self.deposit([-amount for amount in transaction])
            return transaction

        return [-1]


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)