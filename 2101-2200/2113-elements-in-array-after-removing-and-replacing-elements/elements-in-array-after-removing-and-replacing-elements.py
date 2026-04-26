class Solution:
    def elementInNums(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # time, index
        n = len(nums)
        
        ans = []
        cached = []
        for i in range(n):
            cached.append(nums[i:])
        for i in range(n):
            cached.append(nums[:i])
        cycle = len(cached)
        # print(cached)
        for time, index in queries:
            t = time%cycle
            ans.append(cached[t][index] if index<len(cached[t]) else -1)
        return ans 
        
class Solution2:
    def elementInNums(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        def answerQuery(query):
            time, idx = query
            time %= len(nums)*2
            if time <= len(nums):
                return nums[idx+time] if 0 <= idx+time < len(nums) else -1
            else:
                return nums[idx] if 0 <= idx < time-len(nums) else -1
        
        return [answerQuery(query) for query in queries]