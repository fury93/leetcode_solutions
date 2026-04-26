class Solution:
    # DFS to detect cycle nodes and mark them in `is_in_cycle`
    def detect_cycle_nodes(
        self, current_node, adjacency_list, is_in_cycle, visited, parent
    ):
        visited[current_node] = True  # Mark current node as visited
        for neighbor in adjacency_list[current_node]:
            if not visited[neighbor]:
                parent[neighbor] = current_node  # Set parent for backtracking
                if self.detect_cycle_nodes(
                    neighbor, adjacency_list, is_in_cycle, visited, parent
                ):
                    return True  # Return True if cycle detected
            elif parent[current_node] != neighbor:  # Cycle detected
                is_in_cycle[neighbor] = True  # Mark the start of the cycle
                temp_node = current_node
                # Backtrack to mark all nodes in the cycle
                while temp_node != neighbor:
                    is_in_cycle[temp_node] = True
                    temp_node = parent[temp_node]
                return True
        return False  # No cycle found in this path

    # DFS to calculate distances from cycle nodes
    def calculate_distances(
        self,
        current_node,
        current_distance,
        adjacency_list,
        distances,
        visited,
        is_in_cycle,
    ):
        distances[current_node] = (
            current_distance  # Set distance for current node
        )
        visited[current_node] = True  # Mark node as visited
        for neighbor in adjacency_list[current_node]:
            if visited[neighbor]:
                continue  # Skip if already visited
            new_distance = (
                0 if is_in_cycle[neighbor] else current_distance + 1
            )  # Reset if on cycle
            self.calculate_distances(
                neighbor,
                new_distance,
                adjacency_list,
                distances,
                visited,
                is_in_cycle,
            )

    def distanceToCycle(self, n, edges):
        is_in_cycle = [False] * n
        visited = [False] * n
        parent = [0] * n
        distances = [0] * n
        adjacency_list = [[] for _ in range(n)]

        # Build adjacency list for the graph
        for edge in edges:
            adjacency_list[edge[0]].append(edge[1])
            adjacency_list[edge[1]].append(edge[0])

        # Detect and mark cycle nodes
        self.detect_cycle_nodes(0, adjacency_list, is_in_cycle, visited, parent)

        # Reset visited array before distance calculation
        visited = [False] * n

        # Calculate distances starting from any cycle node
        for i in range(n):
            if is_in_cycle[i]:
                self.calculate_distances(
                    i, 0, adjacency_list, distances, visited, is_in_cycle
                )
                break  # Only need to start from one cycle node
        return distances

# Approach 2: Layer By Layer + Multisource BFS
class Solution2:
    def distanceToCycle(self, n, edges):
        # 'is_in_cycle' is initially True for all nodes
        is_in_cycle = [True] * n
        visited = [False] * n
        degree = [0] * n
        distances = [0] * n
        adjacency_list = [[] for _ in range(n)]

        # Build the adjacency list and calculate node degrees
        for edge in edges:
            adjacency_list[edge[0]].append(edge[1])
            adjacency_list[edge[1]].append(edge[0])
            degree[edge[0]] += 1
            degree[edge[1]] += 1

        node_queue = deque()

        # Start by adding all leaf nodes (degree 1) to the queue
        for i in range(n):
            if degree[i] == 1:
                node_queue.append(i)

        # Perform BFS to remove nodes with degree 1, progressively reducing the graph
        while node_queue:
            current_node = node_queue.popleft()
            # Mark the node as not in the cycle
            is_in_cycle[current_node] = False

            # Update the degree of neighbors and add them to the queue if their degree becomes 1
            for neighbor in adjacency_list[current_node]:
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    node_queue.append(neighbor)

        # Add all cycle nodes to the queue and mark them as visited
        for current_node in range(n):
            if is_in_cycle[current_node]:
                node_queue.append(current_node)
                visited[current_node] = True

        # BFS to calculate distances from cycle nodes
        current_distance = 0
        while node_queue:
            # Track number of nodes to process at this distance level
            queue_size = len(node_queue)
            for _ in range(queue_size):
                current_node = node_queue.popleft()
                # Set the distance for the current node
                distances[current_node] = current_distance

                # Add unvisited neighbors to the queue
                for neighbor in adjacency_list[current_node]:
                    if visited[neighbor]:
                        continue
                    node_queue.append(neighbor)
                    visited[neighbor] = True
            # Increment distance after processing all nodes at the current level
            current_distance += 1

        return distances
