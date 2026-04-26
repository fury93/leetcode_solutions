class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        ar, vow = list(s), []
        for c in ar:
            if c in vowels: vow.append(c)
                
        vow.sort()
        
        j = 0
        for i, c in enumerate(ar):
            if c in vowels:
                ar[i] = vow[j]
                j += 1
        
        return ''.join(ar)
        