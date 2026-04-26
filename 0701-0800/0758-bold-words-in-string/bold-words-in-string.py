class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        n = len(s)
        bold = [False for _ in range(n)] 
    
        for word in words:
            start = s.find(word)
            while start != -1:
                end = start + len(word)
                for i in range(start, end):
                    bold[i] = True
                
                start = s.find(word, start + 1)

        ans = []
        for idx, c in enumerate(s):
            if bold[idx] and (idx == 0 or not bold[idx - 1]):
                ans.append("<b>")

            ans.append(c)

            if bold[idx] and (idx == n - 1 or not bold[idx + 1]):
                ans.append("</b>")

        return "".join(ans)
        
class Solution2:
    def boldWords(self, words, S):
        n=len(S)
        b=[False]*n
        for w in words:
            t=S.find(w)
            l=len(w)
            while t>-1:
                for i in range(t,t+l):
                    b[i]=True
                t=S.find(w,t+1)
        ans=''
        i=0
        while i<n:
            if b[i]:
                ans+=r'<b>'
                while i<n and b[i]:
                    ans+=S[i]
                    i+=1
                ans+=r'</b>'
            else:
                ans+=S[i]
                i+=1
        return ans