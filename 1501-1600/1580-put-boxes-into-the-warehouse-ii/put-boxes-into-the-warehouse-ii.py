class Solution:
    def maxBoxesInWarehouse(
        self, boxes: List[int], warehouse: List[int]
    ) -> int:
        n = len(warehouse)
        minHeight = float("inf")
        effectiveHeights = [0] * n

        # Preprocess the height of the warehouse rooms to
        # get usable heights from the left end

        for i in range(n):
            minHeight = min(minHeight, warehouse[i])
            effectiveHeights[i] = minHeight
        minHeight = float("inf")
        # Update the effective heights considering the right end

        for i in range(n - 1, -1, -1):
            minHeight = min(minHeight, warehouse[i])
            effectiveHeights[i] = max(effectiveHeights[i], minHeight)
        # Sort the effective heights of the warehouse rooms

        effectiveHeights.sort()

        # Sort the boxes by height

        boxes.sort()

        count = 0
        boxIndex = 0
        # Try to place each box in the warehouse from
        # the smallest room to the largest

        for i in range(n):
            if boxIndex < len(boxes) and boxes[boxIndex] <= effectiveHeights[i]:
                # Place the box and move to the next one

                count += 1
                boxIndex += 1
        return count

class Solution2:
    def maxBoxesInWarehouse(
        self, boxes: List[int], warehouse: List[int]
    ) -> int:
        # Sort the boxes by height

        boxes.sort()

        warehouse_size = len(warehouse)
        left_index = 0
        right_index = warehouse_size - 1
        box_count = 0
        box_index = len(boxes) - 1

        # Iterate through the boxes from largest to smallest

        while left_index <= right_index and box_index >= 0:
            # Check if the current box can fit in the
            # leftmost available room

            if boxes[box_index] <= warehouse[left_index]:
                box_count += 1
                left_index += 1
            # Check if the current box can fit in the
            # rightmost available room

            elif boxes[box_index] <= warehouse[right_index]:
                box_count += 1
                right_index -= 1
            box_index -= 1
        return box_count