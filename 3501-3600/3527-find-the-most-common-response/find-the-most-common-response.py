class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        freq = defaultdict(int)
        for res in responses:
            for r in set(res):
                freq[r] += 1

        return min(freq, key = lambda k: (-freq[k], k))