class Solution:
    def minOperations(self, logs: List[str]) -> int:
        deep = 0
        for log in logs:
            if log == '../':
                if deep == 0: continue
                deep -= 1
            elif log == './':
                continue
            else:
                deep +=1

        return deep