class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        maxV, minV, errors = 0,0, [] 
        
        # gather minV, maxV and errors  
        for p in prices: 
            fp = float(p)
            f, c = math.floor(fp), math.ceil(fp)
            minV, maxV = minV + f, maxV + c 
            fError, cError = fp - f, c - fp 
            errors.append((fError, cError))
        
        # lets make sure this is actually possible 
        if target < minV or target > maxV: 
            return "-1"        
        
        # The number of prices that need to be rounded up (rest are rounded down)
        ceilCount = target - minV
        
        # Floor errors are enough to give us what we need 
        errors = sorted(errors, reverse=True)
        
        #min error 
        minError = sum(e[1] for e in errors[:ceilCount]) + sum(e[0] for e in errors[ceilCount:])
        
        # return the error
        return "{:.3f}".format(minError)