class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3: return False
        
        isVowel, isConsonant = False, False,
        vowels = set(['a', 'e', 'i', 'o', 'u'])

        for ch in word:
            if not ch.isalnum(): return False
            if ch.isalpha():
                if ch.lower() in vowels:
                    isVowel = True
                else:
                    isConsonant = True
        
        return isVowel and isConsonant