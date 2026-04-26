class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        start, pl = 0, len(part)
        while True:
            pos = s.find(part, start)
            if pos == -1:
                break
            s = s[:pos] + s[pos+pl:]
            start = max(0, pos - pl)
        
        return s

    def removeOccurrences2(self, s: str, part: str) -> str:
        stack, pl, ss = [], len(part), list(part)

        for ch in s:
            stack.append(ch)
            if stack[-pl:] == ss:
                for _ in range(pl): stack.pop()
        
        return ''.join(stack)

            
        