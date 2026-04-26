class Solution:
    def findMaximums(self, nums: List[int]) -> List[int]:
        stack, n = [], len(nums)
        ans = [0] * n
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] >= num:              # ensure mono-increase
                min_idx = stack.pop()                            # min_idx is the `stack_top_idx` we mentioned earlier, smallest between `left` and `right` below
                left, right = (stack[-1] + 1) if stack else 0, i # left & right end of window, left is `second_stack_top_idx + 1`, right is `i`
                window = right - left - 1                        # window_size_idx = window size - 1
                ans[window] = max(ans[window], nums[min_idx])    # update maximum
            stack.append(i)
        else:
            while stack:                                         # at the end of iteration, we want to pop out all elements in stack. Here assuming the `current_value` is super small, so that every number in the stack will be popped out
                min_idx = stack.pop()
                left, right = (stack[-1] + 1) if stack else 0, n
                window = right - left - 1    
                ans[window] = max(ans[window], nums[min_idx])
        for i in range(n-2, -1, -1):                             # update non-touched windows using result for larger windows
            ans[i] = max(ans[i], ans[i+1])
        return ans