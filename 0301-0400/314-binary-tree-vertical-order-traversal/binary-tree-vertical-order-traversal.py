# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        d = collections.defaultdict(list)
        q = collections.deque([(root, 0)])
        minCol = maxCol = 0

        while q:
            node, col = q.popleft()
            d[col].append(node.val)
            minCol = min(minCol, col)
            maxCol = max(maxCol, col)
            if node.left:
                q.append((node.left, col-1))
            if node.right:
                q.append((node.right, col+1))

        return [d[key] for key in range(minCol, maxCol+1)]

# Approach 1: Breadth-First Search (BFS)
class Solution1:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        columnTable = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()

            if node is not None:
                columnTable[column].append(node.val)
                
                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))
                        
        return [columnTable[x] for x in sorted(columnTable.keys())]

# Approach 2: BFS without Sorting
class Solution2:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        columnTable = defaultdict(list)
        min_column = max_column = 0
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()

            if node is not None:
                columnTable[column].append(node.val)
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))

        return [columnTable[x] for x in range(min_column, max_column + 1)]

# Approach 3: Depth-First Search (DFS)
class Solution3:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        columnTable = defaultdict(list)
        min_column = max_column = 0

        def DFS(node, row, column):
            if node is not None:
                nonlocal min_column, max_column
                columnTable[column].append((row, node.val))
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                # preorder DFS
                DFS(node.left, row + 1, column - 1)
                DFS(node.right, row + 1, column + 1)

        DFS(root, 0, 0)

        # order by column and sort by row
        ret = []
        for col in range(min_column, max_column + 1):
            columnTable[col].sort(key=lambda x:x[0])
            colVals = [val for row, val in columnTable[col]]
            ret.append(colVals)

        return ret