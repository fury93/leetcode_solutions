class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))
        
        # one pointers
        l1, l2 = len(word1), len(word2)
        res= []
        for i in range(max(l1, l2)):
            if i < l1: res.append(word1[i])
            if i < l2: res.append(word2[i])
        
        return ''.join(res)