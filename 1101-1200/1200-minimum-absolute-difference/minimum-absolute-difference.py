class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff = float('inf')
        for i, n in enumerate(arr):
            if i > 0 and n != arr[i-1]:
                minDiff = min(minDiff, abs(n - arr[i-1]))
        
        res = []
        for i, n in enumerate(arr):
            if i > 0 and arr[i-1] == n - minDiff:
                res.append([arr[i-1], n])

        return res
