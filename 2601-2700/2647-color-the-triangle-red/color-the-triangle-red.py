class Solution:
    def colorRed(self, n: int) -> List[List[int]]:
        a = [[1, 1]]
        for i, start, short in zip(range(n, 1, -1), cycle((1, 2, 3, 1)), cycle((0, 1))):
            for j in range(start, i * 2, 2):
                a.append([i, j])
                if short:
                    break
        return a

class Solution2:
    def colorRed(self, n: int) -> List[List[int]]:
        ans = [[1, 1]]
        k = 0
        for i in range(n, 1, -1):
            if k == 0:
                for j in range(1, i << 1, 2):
                    ans.append([i, j])
            elif k == 1:
                ans.append([i, 2])
            elif k == 2:
                for j in range(3, i << 1, 2):
                    ans.append([i, j])
            else:
                ans.append([i, 1])
            k = (k + 1) % 4
        return ans