# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

# Approach 1: Depth-First Search On Binary Tree (2 Passes)
class Solution:
    def __init__(self):
        # Hashmap to map old tree's nodes with new tree's nodes.
        self.new_old_pairs: dict[str, int] = {None: None}

    def deep_copy(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if not root:
            return None
        new_root = NodeCopy(root.val)
        # Deep copy left subtree and attach it on new node's left.
        new_root.left = self.deep_copy(root.left)
        # Deep copy right subtree and attach it on new node's right.
        new_root.right = self.deep_copy(root.right)
        # Store the new node and old node's pair in hash map.
        self.new_old_pairs[root] = new_root
        return new_root

    def map_random_pointers(self, old_node: 'Optional[Node]') -> None:
        if not old_node:
            return
        new_node = self.new_old_pairs[old_node]
        old_node_random = old_node.random
        new_node_random = self.new_old_pairs[old_node_random]
        # Map newNode with it's respective random node.
        new_node.random = new_node_random
        # Traverse on rest nodes to map their respective new node's random pointers.
        self.map_random_pointers(old_node.left)
        self.map_random_pointers(old_node.right)

    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        # Create a new tree for each node of old tree and map new node with old respective node.
        new_root = self.deep_copy(root)
        # We will assign random pointers of new tree to respective correct new nodes.
        self.map_random_pointers(root)
        return new_root

# Approach 2: Depth-First Search On Graph (1 Pass)
class Solution2:
    def __init__(self):
        # Hashmap to map old tree's nodes with new tree's nodes.
        self.seen: dict[str, int] = {None: None}
            
    # Function to traverse on the sub graph of 'root'.
    def dfs(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if not root:
            return None

        if self.seen.get(root) is not None:
            return self.seen.get(root)

        new_root = NodeCopy(root.val)
        # Mark old root as seen and store its respective new node.
        self.seen[root] = new_root
        
        # Traverse on all 3 edges of root and attach respective new node
        # to the newRoot.
        new_root.left = self.dfs(root.left)
        new_root.right = self.dfs(root.right)
        new_root.random = self.dfs(root.random)
        return new_root

    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        # Traverse on each node of the given tree.
        new_root = self.dfs(root)
        return new_root

# Approach 3: Breadth-First Search on Graph
class Solution3:
    def __init__(self):
        # Hashmap to map old tree's nodes with new tree's nodes.
        self.seen: dict = {None: None}
            
    # Function to traverse on the sub graph of 'root'.
    def bfs(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if not root:
            return None

        pending = deque()
        # Push root in queue, mark it as seen and, 
        # store its respective new node.
        pending.append(root)
        self.seen[root] = NodeCopy(root.val)
        
        while pending:
            old_node = pending.popleft()
            new_node = self.seen[old_node]
            
            # Traverse on left, right and random edges one-by-one, if nodes exist and, 
            # not already seen then we push it in queue, create a copy and attach it to new node.
            if old_node.left:
                if not old_node.left in self.seen:
                    pending.append(old_node.left)
                    self.seen[old_node.left] = NodeCopy(old_node.left.val)
                new_node.left = self.seen[old_node.left]

            if old_node.right:
                if not old_node.right in self.seen:
                    pending.append(old_node.right)
                    self.seen[old_node.right] = NodeCopy(old_node.right.val)
                new_node.right = self.seen[old_node.right]

            if old_node.random:
                if not old_node.random in self.seen:
                    pending.append(old_node.random)
                    self.seen[old_node.random] = NodeCopy(old_node.random.val)
                new_node.random = self.seen[old_node.random]

        return self.seen[root]

    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        # Traverse on each node of the given tree.
        new_root = self.bfs(root)
        return new_root