class Solution:
    def closestFair(self, n: int) -> int:

        minNum = lambda x: int('1' + '0'*(x//2) + '1'*(x//2-1))
        isFair = lambda x: 2*sum(ord(ch)%2 for ch in str(x)) == len(str(x))

        l = len(str(n))
        if l % 2: return minNum(l+1)    # odd  digit count => go to next even minNum

        pow10 = int('1' + '0'*l)
        for i in range(n,pow10):        # even digit count => look for fair integer with l digits
            if isFair(i): return i      # if found, return the integer

        return minNum(l+2)              #if not, return the least minNum that's greater than n