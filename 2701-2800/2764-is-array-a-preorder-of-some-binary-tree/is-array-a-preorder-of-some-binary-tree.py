class Solution:
    def isPreorder(self, nodes: List[List[int]]) -> bool:
        # The stack starts with the root node
        stack = [nodes[0][0]]
        
        # Iterating over the rest of the nodes
        for i in range(1, len(nodes)):
            node, parent = nodes[i]
            
            # Check if the current node's parent is the node at the top of the stack
            while stack and stack[-1] != parent:
                stack.pop()
                
            # If the stack becomes empty before we find the parent, return False
            if not stack:
                return False
            
            # Add the current node to the stack
            stack.append(node)
            
        # If we've successfully gone through all the nodes, return True
        return True