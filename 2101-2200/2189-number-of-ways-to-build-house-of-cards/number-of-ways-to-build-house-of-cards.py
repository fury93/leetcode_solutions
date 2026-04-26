class Solution:
    def houseOfCards(self, n: int) -> int:
        dp=[1]+[0]*n
        for level_cards in range(2,n+1,3):
            for all_cards in range(n,level_cards-1,-1):
                dp[all_cards]+=dp[all_cards-level_cards]
        return dp[n]