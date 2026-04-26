class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        sm = sum(arr)
        if sm % 3: return False
        
        average, cnt, prefix = sm // 3, 0, 0
        for n in arr:
            prefix += n
            if prefix == average:
                cnt +=1
                if cnt == 3: return True
                prefix = 0
            
        return False

