class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        res = -1
        for key, val in cnt.items():
            if key == val:
                res = max(res, key)
        
        return res