from math import gcd

class Solution:
    def validSubarraySplit(self, n: List[int]) -> int:

        if n[0] == 1 or n[-1] == 1: return -1                   # [1] check for trivial cases (i.e., gcd = 1)
		
        @cache
        def dfs(j):
            if j == len(n): return 0                            # [2] nothing to separate
            return min([dfs(i+1) for i in range(j, len(n))      # [3] get the minimal number of remaining valid subarrays
			                     if  gcd(n[i], n[j]) > 1]       #     for each of separated valid subarrays
                                 or  [float('inf')]) + 1        #     or put a red flag if correct separation is not possible
                    
        return dfs(0) if dfs(0) < float('inf') else -1