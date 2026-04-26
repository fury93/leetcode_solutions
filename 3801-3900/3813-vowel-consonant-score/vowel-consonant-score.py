class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels = set('aeiou')
        consonant = set(string.ascii_lowercase) - vowels

        v = sum(1 for ch in s if ch in vowels)
        c = sum(1 for ch in s if ch in consonant)

        return v//c if c > 0 else 0