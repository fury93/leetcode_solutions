class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        res = []
        d = {k: v for k, v in knowledge}

        isParseKey, key = False, []
        for ch in s:
            if ch == '(':
                isParseKey = True
            elif ch == ')':
                res.append(d.get(''.join(key), '?'))
                key = []
                isParseKey = False
            elif isParseKey:
                key.append(ch)
            else:
                res.append(ch)
        
        return ''.join(res)