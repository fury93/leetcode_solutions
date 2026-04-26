class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        modulo = [0] * k
        for n in arr:
            mod = n % k
            modulo[mod] += 1

        if modulo[0] & 1: return False
        for m in range(1, k // 2 + 1):
            if modulo[k-m] != modulo[m]: return False

        return True