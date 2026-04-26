class Solution:
    def canSortArray(self, nums):
        n = len(nums)
        values = nums.copy()  # Create a copy of the original array

        # First Pass: Iterate from left to right
        # Goal: Move the maximum value of each segment as far right as possible
        for i in range(n - 1):
            if values[i] <= values[i + 1]:
                continue
            else:
                # Check if the current and next element have the same number of set bits
                if bin(values[i]).count("1") == bin(values[i + 1]).count("1"):
                    # Swap if they do
                    temp = values[i]
                    values[i] = values[i + 1]
                    values[i + 1] = temp
                else:
                    return False  # Return false if they cannot be swapped

        # Second Pass: Iterate from right to left
        # Goal: Move the minimum value of each segment as far left as possible
        for i in range(n - 1, 0, -1):
            if values[i] >= values[i - 1]:
                continue
            else:
                # Check if the current and previous element have the same number of set bits
                if bin(values[i]).count("1") == bin(values[i - 1]).count("1"):
                    # Swap if they do
                    temp = values[i]
                    values[i] = values[i - 1]
                    values[i - 1] = temp
                else:
                    return False  # Return false if they cannot be swapped

        # If both passes complete without returning false, the array can be sorted
        return True