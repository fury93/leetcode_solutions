class Solution:
    def digitsCount(self, d, low, high):
        def getCounts(num):
            res, step, n = 0, 1, 0
            while num>0:
                t = num%10 # the current digit
                num = num//10 # the num in front of the digit
                if t>d:# 
                    res+=(1+num-(d==0))*step
                elif t==d:# 
                    res+=(num-(d==0))*step+n+1
                else:
                    res+=(num-(d==0))*step
                n += t*step# update the number after the current digit
                step = 10*step# update the weight
            return res
        
        return getCounts(high)-getCounts(low-1)