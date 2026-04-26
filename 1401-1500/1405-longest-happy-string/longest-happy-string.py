class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        maxHeap = list(filter(lambda x: x[0] < 0, [(-a, 'a'), (-b, 'b'), (-c, 'c')]))
        heapify(maxHeap)
        
        while maxHeap:
            cnt, ch = heappop(maxHeap)
            if len(res) > 1 and res[-1] == ch and res[-2] == ch:
                if not maxHeap: break
                cnt2, ch2 = heappop(maxHeap)
                res.append(ch2)
                cnt2 += 1
                if cnt2 != 0:
                    heappush(maxHeap, (cnt2, ch2))

            res.append(ch)
            cnt +=1
            if cnt != 0:
                heappush(maxHeap, (cnt, ch))

        return ''.join(res)
