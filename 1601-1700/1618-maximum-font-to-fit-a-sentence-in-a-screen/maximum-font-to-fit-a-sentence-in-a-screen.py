# """
# This is FontInfo's API interface.
# You should not implement it, or speculate about its implementation
# """
#class FontInfo(object):
#    Return the width of char ch when fontSize is used.
#    def getWidth(self, fontSize, ch):
#        """
#        :type fontSize: int
#        :type ch: char
#        :rtype int
#        """
# 
#    def getHeight(self, fontSize):
#        """
#        :type fontSize: int
#        :rtype int
#        """
class Solution:
    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo : 'FontInfo') -> int:
        
        def check(fs):
            if fontInfo.getHeight(fs) > h:
                return False
            if sum(fontInfo.getWidth(fs, c) for c in text) > w:
                return False
            return True
        
        l, r = -1, len(fonts) - 1
        while l < r:
            m = r - (r - l) // 2
            if check(fonts[m]):
                l = m
            else:
                r = m - 1
        return fonts[l] if l > -1 else -1