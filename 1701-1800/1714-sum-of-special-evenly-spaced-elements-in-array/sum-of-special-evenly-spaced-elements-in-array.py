class Solution:
    def solve(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        mod = 10**9 + 7
        pre_sum_array = defaultdict()
        
        big_y_pairs = {(xi, yi) for xi, yi in queries if yi > sqrt(n)}
        big_y_pair_sums = {(xi, yi): sum(nums[xi: n: yi]) for xi, yi in big_y_pairs}
        
        pre_sum_array_keys = {(xi % yi, yi) for xi, yi in queries if yi <= sqrt(n)}
        
        for start_point, yi in pre_sum_array_keys: 
            _sum = nums[start_point]
            pre_sum_array[(start_point, yi)] = [0, _sum]
            for x in range(start_point + yi, n, yi):
                _sum += nums[x]
                pre_sum_array[(start_point, yi)].append(_sum)

        return [
            (
                big_y_pair_sums[(xi, yi)] 
                if yi > sqrt(n)
                else pre_sum_array[(xi % yi, yi)][-1] - pre_sum_array[(xi % yi, yi)][xi // yi]
            ) % mod
            for xi, yi in queries
        ]

from sortedcontainers import SortedDict
class Solution2:
    def solve(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        prefs = {}
        n = len(nums)
        MOD = 10**9 + 7


        def get_sum(k, b):
            a = b % k
            if (k,a) not in prefs:
                ssum = 0
                tmp = []
                for i in range(a,n, k):
                    ssum+=nums[i]
                    tmp.append(ssum)
                
                prefs[(k,a)] = tmp
            table = prefs[(k,a)]

            idx = (b-a)//k
            return (table[-1] - (table[idx-1] if idx-1 >= 0 else 0)) % MOD

        def realtime(k,b):
            ssum = 0
            for i in range(b,n,k):
                ssum+=nums[i]
            return ssum % MOD


        out = []
        for b,k in queries:
            if k*k > n:
                out.append(realtime(k,b))
            else:
                out.append(get_sum(k,b))
        return out



