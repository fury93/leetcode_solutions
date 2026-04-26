class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res, L = 0, len(words)
        for i in range(L):
            for j in range(i+1, L):
                lni, lnj = len(words[i]), len(words[j])
                if lni > lnj: continue
                if words[i] == words[j][:lni] and words[i] == words[j][-lni:lnj]:
                    res += 1

        return res