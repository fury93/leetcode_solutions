class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        stack = []
        for w in words:
            key = (sorted(w), w)
            if stack and stack[-1][0] == key[0]: continue
            stack.append(key)
        
        return [w for _, w in stack]

        