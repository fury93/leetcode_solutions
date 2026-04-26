class Solution:
    def reverseWords(self, s: str) -> str:
        vowels = set('aeiou')
        def getVowels(word):
            return sum(1 for ch in word if ch in vowels)
        
        words = s.split()
        swapCnt = getVowels(words[0])

        for i in range(1, len(words)):
            if getVowels(words[i]) == swapCnt:
                words[i] = words[i][::-1]

        return ' '.join(words)