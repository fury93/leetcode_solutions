class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def parse(digits, i):
            if i == len(num):
                return len(digits) >= 3
            
            if len(digits) < 2:
                a, b = None, None
            else:
                *_, a, b = digits

            for j in range(i+1, len(num)+1):
                c = num[i:j]
                # [0 1 1 2] or [1 0 1 1 2] are valid
                if len(c) > 1 and c[0] == '0':
                    break
               
                c = int(c)
                if b is None or a + b == c:
                    digits.append(c)
                    if (parse(digits, j)):
                        return True
                    digits.pop()
            
            return False
                    
        return parse([], 0)
        