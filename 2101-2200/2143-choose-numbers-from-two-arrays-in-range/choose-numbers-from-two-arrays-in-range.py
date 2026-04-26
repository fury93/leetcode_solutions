class Solution:
    def countSubranges(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp = collections.defaultdict(int)
        MOD = 10 ** 9 + 7
        res = 0

        for i in range(n):
            num1, num2 = nums1[i], nums2[i]
            tmp = collections.defaultdict(int)
            tmp[num1] += 1
            tmp[-num2] += 1

            for psum, freq in dp.copy().items():
                tmp[psum + num1] = (tmp[psum + num1] + freq) % MOD
                tmp[psum - num2] = (tmp[psum - num2] + freq) % MOD
            
            res = (res + tmp[0]) % MOD
            dp = tmp
        
        return res
        
                    
class Solution2:
    def countSubranges(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = int(1e9) + 7
        N = len(nums1)
        DP = defaultdict(int)
        ans = 0
        for i in range(N):
            n1 = nums1[i]
            n2 = nums2[i]
            DP2 = defaultdict(int)
            DP2[n1] += 1
            DP2[-n2] += 1
            
            for key, value in DP.copy().items():
                DP2[key + n1] = (DP2[key + n1] + value) % MOD
                DP2[key - n2] = (DP2[key - n2] + value) % MOD
            
            ans = (ans + DP2[0]) % MOD
            DP = DP2

        return ans