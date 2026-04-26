class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k < 0: return self.decrypt(code[::-1], -k)[::-1]
        p = list(accumulate(code + code))
        return [p[i+k] - p[i] for i in range(len(code))]