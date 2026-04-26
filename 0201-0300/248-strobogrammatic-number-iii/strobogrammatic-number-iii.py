class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        maps={"0":"0","1":"1","6":"9","8":"8","9":"6"}
        cl,ch=len(low), len(high)
        if cl>ch or (cl==ch and low>high): return 0
        
        ans=["","0","1","8"]
        count=0
        while ans:
            tmp=[]
            for w in ans:
                if len(w)<ch or (len(w)==ch and w<=high):
                    if len(w)>cl or (len(w)==cl and w>=low):  
                        if len(w)>1 and w[0]=="0":##leading zeros
                            pass
                        else:
                            count+=1
                    
                    if ch-len(w)>=2:                
                        for key in maps:
                            res=key+w+maps[key]
                            tmp.append(res)
            ans=tmp
        return count

class Solution2:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        mp = {
            0: 0,
            1: 1,
            6: 9,
            8: 8,
            9: 6
        }
        val = [0,1,6]
        low = [int(low[i]) for i in range(len(low))]
        high = [int(high[i]) for i in range(len(high))]
        idx = len(low)-1
        while idx>=0:
            if low[idx] > 0:
                break
            idx-=1
        low[idx]-=1
        if idx != -1: 
            for i in range(idx+1, len(low)): low[i] = 9

        def count(arr):
            n = len(arr)
            # if n == 1 and arr[0] == 0: return 1
            @cache
            def go(i, ok, need):
                if i==n//2:
                    if n%2: 
                        res = 0
                        if ok: return 3
                        else: 
                            for v in mp:
                                if v > arr[i] or (n != 1 and i == 0 and v == 0): continue
                                if need: res+=int(v<arr[i])
                                else: res+=int(v==1 or v==8 or v == 0)
                        # print(i, ok, need, res)
                        return res 
                    # print(i, ok, need)
                    if need: return 0
                    return 1
                res = 0
                for v in mp:
                    if (i == 0 and v == 0) or (not ok and v > arr[i]): continue
                    new_ok = (ok or v < arr[i])
                    new_need = True if not new_ok and (mp[v] > arr[n-i-1] or need) else False
                    # print(arr, i, v, new_ok, new_need)
                    res+=go(i+1, new_ok, new_need)
                return res

            tot = go(0, False, False)
            # print(tot)
            for length in range(1, n):
                if length == 1: tot+=3
                else: 
                    if length%2: tot+=4*3*pow(5,(length-3)//2)
                    else: tot+=4*pow(5, (length-2)//2)
            return tot
        # print(count(high))
        # print(count(low))
        # return 0
        return count(high) - count(low)

class Solution3:

	@cache
	def _strobo_qties(self, n: int) -> int:
		return (0, 3, 4)[n] if n < 3 else 3*self._strobo_qties(n - 1) if n&1 == 1 else self._strobo_qties(n - 1) + 2*self._strobo_qties(n - 2)

	def __init__(self) -> None:
		self.trans = str.maketrans('01689', '01986')
		self.nmax = 15 # "1 <= low.length, high.length <= 15"
		self.qties = [self._strobo_qties(x) for x in range(self.nmax + 1)]

	def _strobos_gen(self, n: int, strobos: str='01689', strobos_center: str='018'):
		if n == 1:
			yield from "018"
		else:
			for prod in product(product(strobos, repeat=n//2), strobos_center if n%2 == 1 else ['']):
				left, center = prod
				if left[0] != '0':
					left_str = ''.join(left)
					yield left_str + center + left_str.translate(self.trans)[::-1]

	def strobogrammaticInRange(self, low: str, high: str) -> int:
		res, low_len, high_len = 0, len(low), len(high)
		if low_len == high_len:
			for strob in self._strobos_gen(low_len):
				if low <= strob <= high:
					res += 1
				elif strob > high:
					break
		else:
			for strob in self._strobos_gen(low_len):
				if strob >= low:
					res += 1
			for strob in self._strobos_gen(high_len):
				if strob <= high:
					res += 1
				else:
					break
			res += sum(self.qties[n] for n in range(low_len + 1, high_len))
		return res

class Solution4:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        count = 0
        result = []

        @cache
        def helper(i, allow_zero):
            if i == 0:
                return [""]
            if i == 1:
                return ["0", "1", "8"]
            ans = []
            for num in helper(i-2, True):
                if allow_zero:
                    ans.append("0"+num+"0") 
                ans.append("1"+num+"1")
                ans.append("6"+num+"9")
                ans.append("9"+num+"6")
                ans.append("8"+num+"8")
            return ans
        
        # Generate strobogrammatic numbers for each length from low to high
        for n in range(len(low), len(high) + 1):
            result.extend(helper(n, False))
        
        # Filter numbers outside the range
        for num in result:
            if ((len(num) == len(low) and num < low) or 
                (len(num) == len(high) and num > high)):
                continue
            count += 1
            
        return count