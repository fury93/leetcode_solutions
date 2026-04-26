class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def swap(i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i, j = i + 1, j - 1
        
        l = 0
        for r in range(len(s) + 1):
            if r == len(s) or s[r] == ' ':
                swap(l, r - 1)
                l = r + 1
        
        swap(0, len(s)-1)