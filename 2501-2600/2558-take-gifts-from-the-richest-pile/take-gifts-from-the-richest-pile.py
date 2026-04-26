class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-x for x in gifts]
        heapify(gifts)

        while k > 0:
            cnt = heappop(gifts)
            heappush(gifts, -int(sqrt(-cnt)))
            k -= 1
        
        return sum(gifts) * -1