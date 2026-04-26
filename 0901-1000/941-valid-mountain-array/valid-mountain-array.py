class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        l, r, L = 0, len(arr)-1, len(arr)
        while l + 1 < L and arr[l+1] > arr[l]:
            l += 1
        while r > 0 and arr[r-1] > arr[r]:
            r -= 1
        
        return 0 < l == r < L-1