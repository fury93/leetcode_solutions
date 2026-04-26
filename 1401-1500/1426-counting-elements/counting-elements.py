class Solution:
    def countElements(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        return sum(val for k, val in cnt.items() if k+1 in cnt)