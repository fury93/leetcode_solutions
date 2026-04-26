class Solution:
    def countPairs(self, nums1, nums2):
        N = len(nums1)  # nums2 is the same length

        # Difference[i] stores nums1[i] - nums2[i]
        difference = [nums1[i] - nums2[i] for i in range(N)]
        difference.sort()

        # Count the number of valid pairs
        result = 0
        for i in range(0, N):
            # All indices j following i make a valid pair
            if difference[i] > 0:
                result += N - i - 1
                
            # Binary search to find the first index j
            # that makes a valid pair with i
            else:
                left = i + 1
                right = N - 1
                while left <= right:
                    mid = (left + right) // 2
                    # If difference[mid] is a valid pair, search in left half
                    if difference[i] + difference[mid] > 0:
                        right = mid - 1
                    # If difference[mid] does not make a valid pair, search in right half
                    else:
                        left = mid + 1

                # After the search left points to the first index j that makes
                # a valid pair with i so we count that and all following indices
                result += N - left

        return result

class Solution2:
    def countPairs(self, nums1, nums2):
        N = len(nums1)  # nums2 is the same length

        # Difference[i] stores nums1[i] - nums2[i]
        difference = [nums1[i] - nums2[i] for i in range(N)]
        difference.sort()

        # Count the number of valid pairs
        result = 0
        left = 0
        right = N - 1
        while left < right:
            # Left makes a valid pair with right
            # Right also makes a valid pair with the indices between the pointers
            if difference[left] + difference[right] > 0:
                result += right - left
                right -= 1
            # Left and right are not a valid pair
            else:
                left += 1
        return result