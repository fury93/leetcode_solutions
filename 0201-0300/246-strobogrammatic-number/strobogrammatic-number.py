class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        d = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        i, j = 0, len(num) - 1

        while i <= j:
            if num[i] not in d or d[num[i]] != num[j]:
                return False
            i += 1
            j -= 1
        
        return True

    
    def isStrobogrammatic2(self, num: str) -> bool:
        d = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        num2 = ''.join(d[n] for n in num if n in d)
        
        return num == num2[::-1]