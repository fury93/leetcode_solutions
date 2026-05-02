class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for i in range(len(num)):
            k, num[~i] = divmod(num[~i] + k, 10)
        
        return list(map(int, str(k))) + num if k else num
    
    def addToArrayForm2(self, num: List[int], k: int) -> List[int]:
        if len(str(k)) > len(num):
            num, k = list(map(int, str(k))), int(''.join(map(str, num)))
        
        carry = 0
        for i in reversed(range(len(num))):
            if not k and not carry: break
            k, remainder = divmod(k, 10)
            n = num[i] + carry + remainder
            carry = 0
            if n <= 9:
                num[i] = n
            else:
                carry, num[i] = divmod(n, 10)

        return num if not carry else [carry] + num