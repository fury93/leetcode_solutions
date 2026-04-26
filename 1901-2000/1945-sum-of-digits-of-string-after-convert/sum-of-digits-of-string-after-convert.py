class Solution:
    def getLucky(self, s: str, k: int) -> int:
        S = []
        for ch in s:
            S.append(str(ord(ch) - 96))
        S = ''.join(S)
        
        while k > 0:
            S = sum(map(int, str(S)))
            k -= 1
        
        return S