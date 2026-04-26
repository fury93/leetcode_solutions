from collections import defaultdict
from typing import List

class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        # Step 1: Group numbers by their modulo K
        groups = defaultdict(list)
        for num in nums:
            groups[num % k].append(num)
        
        # Step 2: Count K-free subsets for each group
        total_count = 1  # Start with the empty subset
        for remainder_group in groups.values():
            # Sort each group to handle conflicts (elements that differ by K)
            remainder_group.sort()
            
            # Initialize DP for counting K-free subsets
            prev_include = 1  # Count subsets including the previous element
            prev_exclude = 1  # Count subsets excluding the previous element
            
            for i in range(1, len(remainder_group)):
                if remainder_group[i] - remainder_group[i - 1] == k:
                    # If adjacent elements differ by K, they can't both be in the subset
                    new_include = prev_exclude  # Only include current element if we excluded previous
                    new_exclude = prev_include + prev_exclude
                else:
                    # No conflict, we can choose to include or exclude current element freely
                    new_include = prev_include + prev_exclude
                    new_exclude = prev_include + prev_exclude
                
                prev_include, prev_exclude = new_include, new_exclude
            
            # Total subsets for the group
            group_count = prev_include + prev_exclude
            total_count *= group_count
        
        return total_count

                
class Solution2:
    def countTheNumOfKFreeSubsets(self, A: List[int], k: int) -> int:        
        dp = [1, 2] + [0] * 998
        for i in range(2, 1000):
            dp[i] = 1 + dp[i - 1] + dp[i - 2]

        A.sort()
        chains, cur_list = [], {}

        for a in A:
            if a - k in cur_list:
                cur_list[a - k].append(a)
                cur_list[a] = cur_list.pop(a - k)
            else:
                cur_list[a] = [a]
                chains.append(cur_list[a])

        res = [dp[len(chain) - 1] for chain in chains]

        return functools.reduce(lambda x,y: x * y, [a + 1 for a in res])