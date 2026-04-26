# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def binarySearch(root2, target2):
            if not root2:
                return False
            if root2.val == target2:
                return True
            elif root2.val > target2:
                return binarySearch(root2.left, target2)
            else:
                return binarySearch(root2.right, target2)

        def dfs(root, target):
            if not root:
                return False
            if binarySearch(root2, target - root.val):
                return True
            return dfs(root.left, target) or dfs(root.right, target)

        return dfs(root1, target)

# Approach 3: Hash Set
class Solution3:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def dfs(curr_node, node_set):
            if not curr_node:
                return
            dfs(curr_node.left, node_set)
            node_set.add(curr_node.val)
            dfs(curr_node.right, node_set)
        
        node_set1, node_set2 = set(), set()
        dfs(root1, node_set1)
        dfs(root2, node_set2)
        
        for value1 in node_set1:
            if target - value1 in node_set2:
                return True
        return False

# Approach 4: Two Pointers
class Solution4:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def dfs(curr_node, node_list):
            if not curr_node:
                return
            dfs(curr_node.left, node_list)
            node_list.append(curr_node.val)
            dfs(curr_node.right, node_list)
        
        node_list1, node_list2 = [], []
        dfs(root1, node_list1)
        dfs(root2, node_list2)
        
        pointer1 = 0
        pointer2 = len(node_list2) - 1
        while pointer1 < len(node_list1) and pointer2 >= 0:
            if node_list1[pointer1] + node_list2[pointer2] == target:
                return True
            elif node_list1[pointer1] + node_list2[pointer2] < target:
                pointer1 += 1
            else:
                pointer2 -= 1
        return False

# Approach 5: Morris Traversal
class Solution5:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def morris_traversal(root):
            current = root
            while current:
                if not current.left:

                    # If you're a little confused about the key word 'yield', 
                    # please see the next paragraph for some explanation.
                    yield current.val
                    current = current.right
                else:
                    pre = current.left
                    while pre.right and pre.right != current:
                        pre = pre.right
                    if not pre.right:
                        pre.right = current
                        current = current.left
                    else:
                        pre.right = None
                        yield current.val
                        current = current.right

        def reversed_morris_traversal(root):
            current = root
            while current:
                if not current.right:
                    yield current.val
                    current = current.left
                else:
                    pre = current.right
                    while pre.left and pre.left != current:
                        pre = pre.left
                    if not pre.left:
                        pre.left = current
                        current = current.right
                    else:
                        pre.left = None
                        yield current.val
                        current = current.left
                        
        iterater1 = morris_traversal(root1)
        iterater2 = reversed_morris_traversal(root2)
        value1 = next(iterater1, None)
        value2 = next(iterater2, None)

        while value1 is not None and value2 is not None:
            if value1 + value2 == target:
                return True
            elif value1 + value2 < target:
                value1 = next(iterater1, None)
            else:
                value2 = next(iterater2, None)
        return False