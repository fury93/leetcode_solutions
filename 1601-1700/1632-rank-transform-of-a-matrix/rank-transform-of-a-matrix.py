# Approach 1: Sorting + BFS
class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        # link row to col, and link col to row
        graphs = {}  # graphs[v]: the connection graph of value v
        for i in range(m):
            for j in range(n):
                v = matrix[i][j]
                # if not initialized, initial it
                if v not in graphs:
                    graphs[v] = {}
                if i not in graphs[v]:
                    graphs[v][i] = []
                if ~j not in graphs[v]:
                    graphs[v][~j] = []
                # link i to j, and link j to i
                graphs[v][i].append(~j)
                graphs[v][~j].append(i)

        # put points into `value2index` dict, grouped by connection
        value2index = {}  # {v: [[points1], [points2], ...], ...}
        seen = set()  # mark whether put into `value2index` or not
        for i in range(m):
            for j in range(n):
                if (i, j) in seen:
                    continue
                seen.add((i, j))
                v = matrix[i][j]
                graph = graphs[v]
                # start bfs
                q = [i, ~j]
                rowcols = {i, ~j}  # store visited row and col
                while q:
                    node = q.pop(0)
                    for rowcol in graph[node]:
                        if rowcol not in rowcols:
                            q.append(rowcol)
                            rowcols.add(rowcol)
                # transform rowcols into points
                points = set()
                for rowcol in rowcols:
                    for k in graph[rowcol]:
                        if k >= 0:
                            points.add((k, ~rowcol))
                            seen.add((k, ~rowcol))
                        else:
                            points.add((rowcol, ~k))
                            seen.add((rowcol, ~k))
                if v not in value2index:
                    value2index[v] = []
                value2index[v].append(points)

        answer = [[0]*n for _ in range(m)]  # the required rank matrix
        rowmax = [0] * m  # rowmax[i]: the max rank in i row
        colmax = [0] * n  # colmax[j]: the max rank in j col
        for v in sorted(value2index.keys()):
            # update by connected points with same value
            for points in value2index[v]:
                rank = 1
                for i, j in points:
                    rank = max(rank, max(rowmax[i], colmax[j]) + 1)
                for i, j in points:
                    answer[i][j] = rank
                    # update rowmax and colmax
                    rowmax[i] = max(rowmax[i], rank)
                    colmax[j] = max(colmax[j], rank)

        return answer


# Approach 2: Sorting + DFS
class Solution2:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        # link row to col, and link col to row
        graphs = {}  # graphs[v]: the connection graph of value v
        for i in range(m):
            for j in range(n):
                v = matrix[i][j]
                # if not initialized, initial it
                if v not in graphs:
                    graphs[v] = {}
                if i not in graphs[v]:
                    graphs[v][i] = []
                if ~j not in graphs[v]:
                    graphs[v][~j] = []
                # link i to j, and link j to i
                graphs[v][i].append(~j)
                graphs[v][~j].append(i)

        # put points into `value2index` dict, grouped by connection
        value2index = {}  # {v: [[points1], [points2], ...], ...}
        seen = set()  # mark whether put into `value2index` or not

        def dfs(node, graph, rowcols):
            rowcols.add(node)
            for rowcol in graph[node]:
                if rowcol not in rowcols:
                    dfs(rowcol, graph, rowcols)

        for i in range(m):
            for j in range(n):
                if (i, j) in seen:
                    continue
                seen.add((i, j))
                v = matrix[i][j]
                graph = graphs[v]
                # use dfs to find the connected parts
                rowcols = set()   # store visited row and col
                dfs(i, graph, rowcols)
                dfs(~j, graph, rowcols)
                # transform rowcols into points
                points = set()
                for rowcol in rowcols:
                    for k in graph[rowcol]:
                        if k >= 0:
                            points.add((k, ~rowcol))
                            seen.add((k, ~rowcol))
                        else:
                            points.add((rowcol, ~k))
                            seen.add((rowcol, ~k))
                if v not in value2index:
                    value2index[v] = []
                value2index[v].append(points)

        answer = [[0]*n for _ in range(m)]  # the required rank matrix
        rowmax = [0] * m  # rowmax[i]: the max rank in i row
        colmax = [0] * n  # colmax[j]: the max rank in j col
        for v in sorted(value2index.keys()):
            # update by connected points with same value
            for points in value2index[v]:
                rank = 1
                for i, j in points:
                    rank = max(rank, max(rowmax[i], colmax[j]) + 1)
                for i, j in points:
                    answer[i][j] = rank
                    # update rowmax and colmax
                    rowmax[i] = max(rowmax[i], rank)
                    colmax[j] = max(colmax[j], rank)

        return answer

# Approach 3: Sorting + Union-Find
class Solution3:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        # implement find and union
        def find(UF, x):
            if x != UF[x]:
                UF[x] = find(UF, UF[x])
            return UF[x]

        def union(UF, x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(UF, x)] = find(UF, y)

        # link row and col together
        UFs = {}  # UFs[v]: the Union-Find of value v
        for i in range(m):
            for j in range(n):
                v = matrix[i][j]
                if v not in UFs:
                    UFs[v] = {}
                # union i to j
                union(UFs[v], i, ~j)

        # put points into `value2index` dict, grouped by connection
        value2index = {}
        for i in range(m):
            for j in range(n):
                v = matrix[i][j]
                if v not in value2index:
                    value2index[v] = {}
                f = find(UFs[v], i)
                if f not in value2index[v]:
                    value2index[v][f] = []
                value2index[v][f].append((i, j))

        answer = [[0]*n for _ in range(m)]  # the required rank matrix
        rowmax = [0] * m  # rowmax[i]: the max rank in i row
        colmax = [0] * n  # colmax[j]: the max rank in j col
        for v in sorted(value2index.keys()):
            # update by connected points with same value
            for points in value2index[v].values():
                rank = 1
                for i, j in points:
                    rank = max(rank, max(rowmax[i], colmax[j]) + 1)
                for i, j in points:
                    answer[i][j] = rank
                    # update rowmax and colmax
                    rowmax[i] = max(rowmax[i], rank)
                    colmax[j] = max(colmax[j], rank)

        return answer

