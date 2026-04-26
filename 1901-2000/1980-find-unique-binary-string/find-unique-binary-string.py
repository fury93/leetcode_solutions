class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return "".join("01"[nums[i][i] == '0'] for i in range(len(nums)))
        #return ''.join(['1' if n[i] == '0' else '0' for i, n in enumerate(nums)])