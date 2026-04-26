class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        N = len(colors)                                     # Number of nodes
        incoming, Graph = [0]*N, [[] for _ in range(N)]     # Define count for incoming edges, graph
        for _, v in edges: incoming[v]+=1                   # Count incoming edges
        for u, v in edges: Graph[u].append(v)               # Code the graph
        stack = [u for u in range(N) if incoming[u]==0]     # Populate stack with the nodes without incoming edges
        cnts = [[0]*26 for _ in range(N)]                   # Max. colors along all the incoming paths for the node 

        while stack:                                        # While we have nodes to process
            u = stack.pop()                                 # Pop the next node to process
            cnts[u][ord(colors[u])-ord('a')] += 1           # Increment the color of the node itself
            for v in Graph[u]:                              # For all outgoing edges of the node
                cnts[v] = list(map(max, cnts[v], cnts[u]))  # Update max. colors of the outgoing node
                incoming[v] -= 1                            # Decrement the counter of edges for the outgoing node
                if incoming[v]==0: stack.append(v)          # If outgoing node has no more incoming edges, add to the stack

        return -1 if sum(incoming)>0 else max([max(node) for node in cnts])