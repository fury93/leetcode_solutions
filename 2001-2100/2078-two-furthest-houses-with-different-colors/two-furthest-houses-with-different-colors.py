class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        l, r, L = 0, len(colors)-1, len(colors)
        while colors[-1] == colors[l]: l +=1
        while colors[0] == colors[r]: r-=1

        return max(r, L-1-l)