class Solution:
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        # Store the data in a hashmap, with the coordinates as the key and the node value as the value
        coord_map = {}
        for element in nums:
            coordinates = element // 10
            value = element % 10
            coord_map[coordinates] = value

        # Pass the initial sum value in the sum function.
        return self.dfs(nums[0] // 10, 0, coord_map)

    def dfs(self, root_coordinates, pre_sum, coord_map):
        # Find the level and position values from the coordinates.
        level = root_coordinates // 10
        position = root_coordinates % 10

        # Find out the left child and right child positions of the tree.
        left = (level + 1) * 10 + position * 2 - 1
        right = (level + 1) * 10 + position * 2
        curr_sum = pre_sum + coord_map[root_coordinates]

        # If left child and right child do not exist, return.
        if not left in coord_map and not right in coord_map:
            return curr_sum

        # Otherwise iterate through the left and right children recursively using depth first search.
        left_sum = (
            self.dfs(left, curr_sum, coord_map) if left in coord_map else 0
        )
        right_sum = (
            self.dfs(right, curr_sum, coord_map) if right in coord_map else 0
        )
        return left_sum + right_sum

class Solution2:
    def pathSum(self, nums: List[int]) -> int:
        map = (
            {}
        )  # Store the node values in a hashmap, using coordinates as the key.

        # Iterate over given nums
        for element in nums:
            coordinates = element // 10
            value = element % 10
            map[coordinates] = value

        total_sum = 0  # Initialize the total sum
        q = [
            (nums[0] // 10, map[nums[0] // 10])
        ]  # Initialize the BFS queue and start with the root node.

        # Continue till queue is not empty
        while q:
            coordinates, current_sum = q.pop(0)  # Dequeue
            level = coordinates // 10
            position = coordinates % 10

            left = (level + 1) * 10 + position * 2 - 1
            right = (level + 1) * 10 + position * 2

            # If it's a leaf node (no left and right children), add currentSum to totalSum.
            if not (left in map or right in map):
                total_sum += current_sum

            # Add the left child to the queue if it exists.
            if left in map:
                q.append((left, current_sum + map[left]))

            # Add the right child to the queue if it exists.
            if right in map:
                q.append((right, current_sum + map[right]))

        return total_sum