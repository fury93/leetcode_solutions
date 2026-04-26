class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtracking(subset, start):
            result.append(subset.copy())
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtracking(subset, i+1)
                subset.pop()
        
        backtracking([], 0)
        return result

    def subsets3(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for n in nums:
            result += [subset + [n] for subset in result]
           
        return result
    
    def subsets2(self, nums: List[int]) -> List[List[int]]:
        result, subset = [], []
        
        def backtracking(i):
            if i == len(nums):
                result.append(subset.copy())
                return
            
            subset.append(nums[i])
            backtracking(i+1)
            subset.pop()
            backtracking(i+1)
        
        backtracking(0)

        return result
