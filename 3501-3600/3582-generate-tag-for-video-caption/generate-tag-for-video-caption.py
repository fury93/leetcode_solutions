class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.split()
        if not words: return '#'
        words[0] = '#' + words[0]
        tag = ''.join(s.capitalize() for s in words)
        return tag[:100]