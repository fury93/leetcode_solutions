class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = 'aeiou'
        freq, pos = defaultdict(int), dict()
        for i, ch in enumerate(s):
            if ch in vowels:
                freq[ch] += 1
                pos.setdefault(ch, i)
        
        vowelOrder = sorted(freq, key=lambda k: (-freq[k], pos[k]))
        
        res, i = [], 0
        for ch in s:
            if ch not in vowels:
                res.append(ch)
                continue
            
            if freq[vowelOrder[i]] == 0:
                i += 1

            vowel = vowelOrder[i]
            res.append(vowel)
            freq[vowel] -= 1

        return ''.join(res)