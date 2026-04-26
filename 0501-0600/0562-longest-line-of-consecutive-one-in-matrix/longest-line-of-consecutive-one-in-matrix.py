class Solution:
    def longestLine(self, A):
        if not A: return 0
        
        def score(line):
            return max(len(list(v)) if k else 0 
                    for k, v in itertools.groupby(line))
        
        groups = collections.defaultdict(list)
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                groups[0, r] += [val]
                groups[1, c] += [val]
                groups[2, r+c] += [val]
                groups[3, r-c] += [val]
        
        return max(map(score, groups.values()))

class Solution2:
    def longestLine(self, M: List[List[int]]) -> int:
        if not M or not M[0]:
            return 0
        res = 0
        row = [0] * len(M)
        col = [0] * len(M[0])
        diag = [0] * (len(M) + len(M[0]) - 1)
        anti_diag = [0] * (len(M) + len(M[0]) - 1)
        
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
                    diag[i-j+len(M[0])-1] += 1
                    anti_diag[i+j] += 1
                    res = max(res, row[i], col[j], diag[i-j+len(M[0])-1], anti_diag[i+j])
                else:
                    row[i] = 0
                    col[j] = 0
                    diag[i-j+len(M[0])-1] = 0
                    anti_diag[i+j] = 0
        return res