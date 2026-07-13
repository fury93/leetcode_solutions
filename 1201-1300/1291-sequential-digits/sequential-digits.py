class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res, digits = [], '123456789'

        for i in range(len(digits)-1):
            for j in range(i + 1, len(digits)):
                n = int(digits[i:j+1])
                if low <= n <= high:
                    res.append(n)
                    
        return sorted(res)