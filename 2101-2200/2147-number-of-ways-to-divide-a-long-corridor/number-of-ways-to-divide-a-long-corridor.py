class Solution:
    def numberOfWays(self, C):
        places = [i for i, x in enumerate(C) if C[i] == "S"]
        m = len(places)
        if m % 2 == 1 or m < 2: return 0
        
        ans = 1
        for i in range(m//2 - 1):
            ans = (ans * (places[2*i+2] - places[2*i+1])) % (10**9 + 7)
        return ans