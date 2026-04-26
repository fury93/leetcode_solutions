class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        count = 0
        def dfs(node):
            nonlocal count
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            left = dfs(node.left)
            right = dfs(node.right)
            count += sum(l + r <= distance for l in left for r in right)
            return [n + 1 for n in left + right if n + 1 < distance]
        dfs(root)
        return count