class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(nodes):
            if parent[i] != -1:
                graph[parent[i]].append(i)

        def dfs(root):  # sum, cnt of remain nodes after deleted
            totalSum = value[root]
            totalNodes = 1
            for nei in graph[root]:
                childSum, childCnt = dfs(nei)
                totalSum += childSum
                totalNodes += childCnt

            if totalSum == 0:
                totalNodes = 0  # This subtree should be removed, so don't count nodes of this subtree
            return totalSum, totalNodes

        return dfs(0)[1]