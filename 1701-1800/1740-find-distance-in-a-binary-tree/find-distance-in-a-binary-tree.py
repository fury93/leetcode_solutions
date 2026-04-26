class Solution:
    def findDistance(self, root, p, q):
        return self.__distance(root, p, q, 0)

    # Private helper function
    def __distance(self, root, p, q, depth):
        if root is None or p == q:
            return 0

        # If either p or q is found, calculate the ret_distance as the maximum
        # of depth and ret_distance value for left and right subtrees.
        if root.val == p or root.val == q:
            left = self.__distance(root.left, p, q, 1)
            right = self.__distance(root.right, p, q, 1)

            return max(left, right) if left > 0 or right > 0 else depth

        # Otherwise, calculate the ret_distance as sum of ret_distance of left
        # and right subtree.
        left = self.__distance(root.left, p, q, depth + 1)
        right = self.__distance(root.right, p, q, depth + 1)
        ret_distance = left + right

        # If current node is the LCA, subtract twice of depth.
        if left != 0 and right != 0:
            ret_distance -= 2 * depth

        return ret_distance

class Solution1:
    def findDistance(self, root, p, q):
        # Find the lowest common ancestor of p and q.
        lca = self.__find_LCA(root, p, q)
        return self.__depth(lca, p) + self.__depth(lca, q)

    # Function to find the LCA of the given nodes.
    def __find_LCA(self, root, p, q):
        if root is None or root.val == p or root.val == q:
            return root
        left = self.__find_LCA(root.left, p, q)
        right = self.__find_LCA(root.right, p, q)
        if left is not None and right is not None:
            return root
        return left if left is not None else right

    # Function to find the depth of the node with respect to LCA.
    def __depth(self, root, target, current_depth=0):
        # Node not found
        if root is None:
            return -1
        if root.val == target:
            return current_depth

        # Check left subtree
        left_depth = self.__depth(root.left, target, current_depth + 1)
        if left_depth != -1:
            return left_depth

        # If not in left subtree, it is guaranteed to be in right subtree
        return self.__depth(root.right, target, current_depth + 1)

class Solution2:
    def findDistance(self, root, p, q):
        lca = self._find_LCA(root, p, q)
        bfs = deque([lca])
        distance = 0
        depth = 0
        foundp = False
        foundq = False
        while bfs and (not foundp or not foundq):
            size = len(bfs)
            for i in range(size):
                node = bfs.popleft()  # Dequeue the node
                if node.val == p:
                    distance += depth
                    foundp = True
                if node.val == q:
                    distance += depth
                    foundq = True
                if node.left:
                    bfs.append(node.left)  # Enqueue left child
                if node.right:
                    bfs.append(node.right)  # Enqueue right child
            depth += 1
        return distance

    def _find_LCA(self, root, p, q):
        if root is None or root.val == p or root.val == q:
            return root
        left = self._find_LCA(root.left, p, q)
        right = self._find_LCA(root.right, p, q)
        if left and right:
            return root
        return left if left else right