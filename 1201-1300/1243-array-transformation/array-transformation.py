class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        hasChanges = True
        while hasChanges:
            hasChanges = False
            resArr = arr.copy()
            for i in range(1, len(arr) - 1):
                if arr[i-1] < arr[i] > arr[i+1]:
                    resArr[i] -= 1
                    hasChanges = True
                elif arr[i-1] > arr[i] < arr[i+1]:
                    resArr[i] += 1
                    hasChanges = True
            arr = resArr
        return arr
            