# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        dq = collections.deque([root])
        for depth, a in enumerate(arr):
            for _ in range(len(dq)):
                node = dq.popleft()
                if node and node.val == a:
                    if depth + 1 == len(arr) and node.left == node.right == None:
                        return True
                    dq.extend(child for child in (node.left, node.right) if child)
        return False