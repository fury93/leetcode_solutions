class DisjointSet:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.island_size = [1] * n

    # Function to find the root of a node with path compression
    def find_root(self, node: int) -> int:

        if self.parent[node] == node:
            return node

        self.parent[node] = self.find_root(self.parent[node])
        return self.parent[node]

    # Function to union two sets based on size
    def union_nodes(self, node_a: int, node_b: int):

        root_a = self.find_root(node_a)
        root_b = self.find_root(node_b)

        # Already in the same set
        if root_a == root_b:
            return

        # Union by size: Attach the smaller island to the larger one
        if self.island_size[root_a] < self.island_size[root_b]:
            # Attach root_a to root_b
            self.parent[root_a] = root_b
            # Update size of root_b's island
            self.island_size[root_b] += self.island_size[root_a]
        else:
            # Attach root_b to root_a
            self.parent[root_b] = root_a
            # Update size of root_a's island
            self.island_size[root_a] += self.island_size[root_b]


class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        # Initialize DSU for the entire grid
        ds = DisjointSet(rows * columns)

        # Direction vectors for traversing up, down, left, and right
        row_directions = [1, -1, 0, 0]
        column_directions = [0, 0, 1, -1]

        # Step 1: Union adjacent `1`s in the grid
        for current_row in range(rows):
            for current_column in range(columns):
                if grid[current_row][current_column] == 1:

                    # Flatten 2D index to 1D
                    current_node = (columns * current_row) + current_column

                    for direction in range(4):
                        neighbor_row = current_row + row_directions[direction]
                        neighbor_column = (
                            current_column + column_directions[direction]
                        )

                        # Check bounds and ensure the neighbor is also `1`
                        if (
                            0 <= neighbor_row < rows
                            and 0 <= neighbor_column < columns
                            and grid[neighbor_row][neighbor_column] == 1
                        ):
                            neighbor_node = (
                                columns * neighbor_row + neighbor_column
                            )

                            ds.union_nodes(current_node, neighbor_node)

        # Step 2: Calculate the maximum possible island size
        max_island_size = 0

        # Flag to check if there are any zeros in the grid
        has_zero = False

        # To store unique roots for a `0`'s neighbors
        unique_roots = set()

        for current_row in range(rows):
            for current_column in range(columns):
                if grid[current_row][current_column] == 0:
                    has_zero = True

                    # Start with the flipped `0`
                    current_island_size = 1

                    for direction in range(4):
                        neighbor_row = current_row + row_directions[direction]
                        neighbor_column = (
                            current_column + column_directions[direction]
                        )

                        # Check bounds and ensure the neighbor is `1`
                        if (
                            0 <= neighbor_row < rows
                            and 0 <= neighbor_column < columns
                            and grid[neighbor_row][neighbor_column] == 1
                        ):
                            neighbor_node = (
                                columns * neighbor_row + neighbor_column
                            )

                            root = ds.find_root(neighbor_node)
                            unique_roots.add(root)

                    # Sum up the sizes of unique neighboring islands
                    for root in unique_roots:
                        current_island_size += ds.island_size[root]

                    # Clear the set for the next `0`
                    unique_roots.clear()

                    # Update the result with the largest island size found
                    max_island_size = max(max_island_size, current_island_size)

        # If there are no zeros, the largest island is the entire grid
        if not has_zero:
            return rows * columns
        return max_island_size