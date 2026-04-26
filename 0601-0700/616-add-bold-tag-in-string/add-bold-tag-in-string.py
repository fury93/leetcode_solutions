class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        n = len(s)
        bold = [False] * n
        
        for word in words:
            start = s.find(word)
            while start != -1:
                for i in range(start, start + len(word)):
                    bold[i] = True
                    
                start = s.find(word, start + 1)

        open_tag = "<b>"
        close_tag = "</b>"
        ans = []
        
        for i in range(n):
            if bold[i] and (i == 0 or not bold[i - 1]):
                ans.append(open_tag)
                
            ans.append(s[i])
            
            if bold[i] and (i == n - 1 or not bold[i + 1]):
                ans.append(close_tag)
        
        return "".join(ans)
        
class Solution2:
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        status = [False]*len(s)
        final = ""
        for word in dict:
            start = s.find(word)
            last = len(word)
            while start != -1:
                for i in range(start, last+start):
                    status[i] = True
                start = s.find(word,start+1)
        i = 0
        i = 0
        while i < len(s):
            if status[i]:
                final += "<b>"
                while i < len(s) and status[i]:
                    final += s[i]
                    i += 1
                final += "</b>"
            else:
                final += s[i]
                i += 1
        return final
                