class Solution:
    def maximumSwap(self, num: int) -> int:
        # if decreasing it's max number, don't need swap 54321
        # find pos i where decreasing is stoped
        # find max value index r from right by i
        # find most left value index l from left by i which less than num[r]
        # swap K and M
        digits = list(str(num))
        L = len(digits)
        for i in range(L-1):
            if digits[i] < digits[i+1]: break
        else: return num
        
        r, maxVal = i+1, digits[i+1]
        for j in range(i+1, L):
            if digits[j] >= maxVal:
                maxVal = digits[j]
                r = j
       
        for l in range(i+1):
            if digits[l] < maxVal:
                digits[l], digits[r] = digits[r], digits[l]
                break
        
        return int(''.join(digits))
        
