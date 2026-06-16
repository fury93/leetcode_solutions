class Solution:
    def processStr(self, s: str) -> str:
        ans = ""
        for i in s:
            if i.islower():
                ans += i
            elif i == '*':
                if ans:
                    ans = ans[:-1]            
            elif i == '#':
                ans += ans
            elif i == '%':
                ans = ans[::-1]
        return ans

    def processStr2(self, s: str) -> str:
        result = []
        for ch in s:
            if ch == "*":
                if result:
                    result.pop()
            elif ch == "#":
                result += result.copy()
            elif ch == "%":
                result = result[::-1]
            else:
                result.append(ch)
        return "".join(result)