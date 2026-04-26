class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_right = [-1]*len(nums)
        curr = ans = 0
        for i in range(len(nums)-1,-1,-1):
            if nums[i] >= curr:
                curr = nums[i]
            else:
                max_right[i] = curr
        stack = []
        for i in sorted(range(len(nums)), key = lambda x: (nums[x], -x)):
            while stack and stack[-1] > i:
                stack.pop()
            if stack and max_right[i] >= 0:
                ans = max(ans, nums[stack[-1]]-nums[i]+max_right[i])
            stack.append(i)
        return ans