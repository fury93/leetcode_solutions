class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[bool]:
        component = [0] * n
        current_component = 0

        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                current_component += 1
            component[i] = current_component
            
        ans = []
        for u, v in queries:
            ans.append(component[u] == component[v])
            
        return ans
