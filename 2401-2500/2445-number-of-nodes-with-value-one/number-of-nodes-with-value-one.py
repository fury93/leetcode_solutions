class Solution:
    def numberOfNodes(self, n: int, queries: List[int]) -> int:
        
        flips = [0 for i in range(n+1)]
        nodes_with_one = 0
        
        # [1] count flips of parent nodes
        for q in queries: flips[q] += 1
        
        # [2] propagate flips to child nodes
        for i in range(1,n+1): flips[i] += flips[i//2]
        
        # [3] count flipped nodes
        for i in range(1,n+1): nodes_with_one += flips[i] % 2
        
        return nodes_with_one