class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        zeros = k
        for n in nums:
            if n == 1:
                if zeros < k: return False
                zeros = 0
            else:
                zeros +=1
        return True
        