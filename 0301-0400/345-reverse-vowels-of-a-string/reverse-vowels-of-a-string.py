class Solution:
    def reverseVowels(self, s: str) -> str:
        chars = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        l, r = 0, len(chars) - 1

        while l < r:
            if chars[l] not in vowels:
                l += 1
            if chars[r] not in vowels:
                r -= 1
            if chars[l] in vowels and chars[r] in vowels:
                chars[l], chars[r] = chars[r], chars[l]
                l += 1
                r -= 1
            
        return ''.join(chars)
            

