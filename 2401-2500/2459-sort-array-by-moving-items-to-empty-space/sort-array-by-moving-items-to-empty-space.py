class Solution:
    def sortArray(self, nums):
    
        n = len(nums)
        pos = [0]*n
        for i, k in enumerate(nums): pos[k] = i      # [1] enumerate positions of elements in 'nums'
        
        def permute(pos, s):                         # [2] this function realises a minimal permutation 
            cnt, nxt = 0, 1                          #     scheme for both 0-indexed and 1-indexed arrays 
            
            while nxt < n:
                if pos[0] == s * (n-1):              # [3] if '0' was found in one of terminal positions 
                    while pos[nxt] == nxt-s:         #     (0 or n-1) then we have to swap '0' with the 
                        nxt += 1                     #     first incorrectly placed number
                        if nxt == n: return cnt      # [4] or return if all numbers are now in order 
                    ni = nxt
                else: ni = pos[0] + s                # [5] '0' was found in a regular (non-terminal) position
                
                pos[0], pos[ni] = pos[ni], pos[0]    # [6] here, the swap happens
                cnt += 1   
                
        return min(permute(list(pos), 0),            # [7] try permuting using both indexing schemes, 
                   permute(list(pos), 1))            #     then choose the minimal result