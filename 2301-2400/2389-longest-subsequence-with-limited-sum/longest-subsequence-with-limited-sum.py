class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        prefix = list(accumulate(sorted(nums)))
        return [bisect_right(prefix, q) for q in queries]


    def answerQueries2(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        
        def bs_pos(maxSum):
            l, r = 0, len(nums)-1
            while l <= r:
                mid = l + (r-l)//2
                val = nums[mid]
                if val < maxSum:
                    l = mid + 1
                elif val > maxSum:
                    r = mid - 1
                else:
                    return mid+1
            return l

        res = []
        for maxSum in queries:
            res.append(bs_pos(maxSum))

        return res