class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(comb, start, remain):
            if remain == 0 and len(comb) == k:
                res.append(comb.copy())
                return
            elif remain < 0 or len(comb) == k:
                return
            
            for i in range(start, 10):
                comb.append(i)
                dfs(comb, i + 1, remain - i)
                comb.pop() 
        
        res = []
        dfs([], 1, n)

        return res