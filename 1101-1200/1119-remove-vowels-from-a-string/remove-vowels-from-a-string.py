class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = set('aeiou')
        return ''.join(ch for ch in s if ch not in vowels)
        