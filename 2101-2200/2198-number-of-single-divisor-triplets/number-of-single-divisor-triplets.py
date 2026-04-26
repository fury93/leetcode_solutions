class Solution:
  def singleDivisorTriplet(self, nums: List[int]) -> int:
    cnts, res =  Counter(nums), 0

    for v1, n1 in cnts.items():
      for v2, n2 in cnts.items():
        for v3, n3 in cnts.items():
          s = v1 + v2 + v3
          if s % v1 == 0 and s % v2 != 0 and s % v3 != 0: 
            if v3 == v2:
              res += n2 * (n2 - 1) * n1
            else:
              res += n1 * n2 * n3 
    
    return res * 3

class Solution2:
    def singleDivisorTriplet(self, nums: List[int]) -> int:
        ans = 0 
        freq = Counter(nums)
        for k0, v0 in freq.items(): 
            for k1, v1 in freq.items(): 
                for k2, v2 in freq.items(): 
                    sm = k0+k1+k2
                    if not sm % k0 and sm % k1 and sm % k2: 
                        if k1 == k2: ans += v0*v1*(v1-1)
                        else: ans += v0*v1*v2 
        return ans*3