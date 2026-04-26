class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, k, zeros = 0, 1, 0
        for n in nums:
            zeros += n == 0
            if zeros > k:
                zeros -= nums[l] == 0
                l += 1
        return len(nums) - l

class Solution1:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest_sequence = 0
        for left in range(len(nums)):
            num_zeroes = 0
            for right in range(left, len(nums)):   # Check every consecutive sequence
                if num_zeroes == 2:
                    break
                if nums[right] == 0:               # Count how many 0's
                    num_zeroes += 1
                if num_zeroes <= 1:                 # Update answer if it's valid
                    longest_sequence = max(longest_sequence, right - left + 1)
        return longest_sequence

class Solution2:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest_sequence = 0
        left, right = 0, 0
        num_zeroes = 0

        while right < len(nums):   # While our window is in bounds
            if nums[right] == 0:    # Increase num_zeroes if the rightmost element is 0
                num_zeroes += 1

            while num_zeroes == 2:   # If our window is invalid, contract our window
                if nums[left] == 0:    
                    num_zeroes -= 1
                left += 1

            longest_sequence = max(longest_sequence, right - left + 1)   # Update our longest sequence answer
            right += 1   # Expand our window

        return longest_sequence