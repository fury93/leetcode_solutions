class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1
        # check if possible to create palindrome, count of odd symbols max is 1
        if sum(cnt & 1 for cnt in freq) > 1: return []

        # remove half of symbols and find a single odd symbol if exists
        singleChar = ''
        for i, cnt in enumerate(freq):
            if cnt & 1:
                singleChar = chr(i + 97)
            freq[i] = cnt // 2 
        
        res, maxLen = [], sum(freq)

        def backtrack(perm):
            if len(perm) == maxLen:
                res.append(''.join(perm + [singleChar] + perm[::-1]))
                return
            
            for i in range(len(freq)):
                if freq[i] > 0:
                    perm.append(chr(i + 97))
                    freq[i] -= 1
                    backtrack(perm)
                    perm.pop()
                    freq[i] += 1

        backtrack([])

        return res