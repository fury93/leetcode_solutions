class Solution:
    def maxTastiness(self, price: List[int], tastiness: List[int], maxAmount: int, maxCoupons: int) -> int:
        
        ## [buy without coupon, no-buy, buy with coupon] are the only 3 options for each fruit
        n = len(price)
        
        @cache
        def find_ans(indx, ma, mc):
            if indx == n:
                return 0
            
            else:
                ans = 0
                
                ans = max(ans, find_ans(indx+1,ma,mc)) ## do not buy this fruit

                if ma >= price[indx]: ## buy this fruit without coupon
                    ans = max(ans, tastiness[indx] + find_ans(indx+1, ma-price[indx], mc))


                if mc >= 1 and ma >= price[indx]//2: ## buy this fruit with coupon
                    ans = max(ans, tastiness[indx] + find_ans(indx+1, ma-(price[indx]//2), mc-1))

            return ans

        return find_ans(0, maxAmount, maxCoupons)