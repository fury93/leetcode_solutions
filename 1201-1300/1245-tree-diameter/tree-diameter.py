# Approach 1: Farthest Nodes via BFS
class Solution1:
    def treeDiameter(self, edges: List[List[int]]) -> int:

        # build the adjacency list representation of the graph
        graph = [set() for i in range(len(edges)+1)]
        for edge in edges:
            u, v = edge
            graph[u].add(v)
            graph[v].add(u)

        def bfs(start):
            """
             return the farthest node from the 'start' node
               and the distance between them.
            """
            visited = [False] * len(graph)

            visited[start] = True
            queue = deque([start])
            distance = -1
            last_node = start
            while queue:
                next_queue = deque()
                while queue:
                    next_node = queue.popleft()
                    for neighbor in graph[next_node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            next_queue.append(neighbor)
                            last_node = neighbor
                distance += 1
                queue = next_queue

            return last_node, distance

        # 1). find one of the farthest nodes
        farthest_node, distance_1 = bfs(0)
        # 2). find the other farthest node
        #  and the distance between two farthest nodes
        another_farthest_node, distance_2 = bfs(farthest_node)

        return distance_2

# Approach 2: Centroids of Graph via BFS
class Solution2:
    def treeDiameter(self, edges: List[List[int]]) -> int:

        # build the adjacency list representation of the graph.
        graph = [set() for i in range(len(edges)+1)]
        for edge in edges:
            u, v = edge
            graph[u].add(v)
            graph[v].add(u)

        # find the outer most nodes, _i.e._ leaf nodes
        leaves = []
        for vertex, links in enumerate(graph):
            if len(links) == 1:
                leaves.append(vertex)

        # "peel" the graph layer by layer,
        #   until we have the centroids left.
        layers = 0
        vertex_left = len(edges) + 1
        while vertex_left > 2:
            vertex_left -= len(leaves)
            next_leaves = []
            for leaf in leaves:
                # the only neighbor left on the leaf node.
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    next_leaves.append(neighbor)
            layers += 1
            leaves = next_leaves

        return layers * 2 + (0 if vertex_left == 1 else 1)

# Approach 3: DFS (Depth-First Search)
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:

        # build the adjacency list representation of the graph.
        graph = [set() for i in range(len(edges)+1)]
        for edge in edges:
            u, v = edge
            graph[u].add(v)
            graph[v].add(u)

        diameter = 0

        def dfs(curr, visited):
            """
                return the max distance
                  starting from the 'curr' node to its leaf nodes
            """
            nonlocal diameter

            # the top 2 distance starting from this node
            top_1_distance, top_2_distance = 0, 0

            distance = 0
            visited[curr] = True

            for neighbor in graph[curr]:
                if not visited[neighbor]:
                    distance = 1 + dfs(neighbor, visited)

                if distance > top_1_distance:
                    top_1_distance, top_2_distance = distance, top_1_distance
                elif distance > top_2_distance:
                    top_2_distance = distance

            # with the top 2 distance, we can update the current diameter
            diameter = max(diameter, top_1_distance + top_2_distance)

            return top_1_distance

        visited = [False for i in range(len(graph))]
        dfs(0, visited)

        return diameter