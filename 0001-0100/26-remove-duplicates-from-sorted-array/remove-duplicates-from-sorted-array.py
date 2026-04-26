class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        snowBall = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                snowBall += 1
            else:
                nums[i - snowBall] = nums[i]

        return len(nums) - snowBall
    
    def removeDuplicates3(self, nums: List[int]) -> int:
        insertPos = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[insertPos] = nums[i]
                insertPos += 1

        return insertPos

    def removeDuplicates2(self, nums: List[int]) -> int:
        lastUniqId = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[lastUniqId]:
                lastUniqId+=1
                nums[lastUniqId] = nums[i]

        return lastUniqId+1
        