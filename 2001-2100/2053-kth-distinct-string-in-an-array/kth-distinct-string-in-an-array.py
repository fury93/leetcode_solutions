class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnt = Counter(arr)

        for key, val in cnt.items():
            if val == 1:
                k -=1
                if k == 0: return key
        
        return ''