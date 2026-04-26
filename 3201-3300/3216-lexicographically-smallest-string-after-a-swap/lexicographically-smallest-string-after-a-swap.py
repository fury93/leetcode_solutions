class Solution:
    def getSmallestString(self, s: str) -> str:
        chars = list(map(int, s))
        for i in range(len(chars)-1):
            if chars[i] & 1 == chars[i+1] & 1 and chars[i] > chars[i+1]:
                chars[i], chars[i+1] = chars[i+1], chars[i]
                break

        return ''.join(map(str,chars))