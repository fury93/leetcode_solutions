class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # sentinel
        arr.append(float("inf"))
        arr.insert(0, 0)
        
        left = 0
        right = len(arr) - 1
        shortest = float("inf")
        # find longest ascending array at left side.
        while left < len(arr) - 2 and arr[left] <= arr[left + 1]:
            left += 1
            
        # [0, 1, 2, 3, 10, 4, 2, 3, 5, ∞]
        #               ↑              
        #             left           
        
        # move right pointer while moving left pointer.
        while left >= 0:
            while right - 1 > left and arr[right - 1] >= arr[left] and arr[right] >= arr[right - 1]:
                right -= 1
            shortest = min(shortest, right - left - 1)
            left -= 1
            
        # [0, 1, 2, 3, 10, 4, 2, 3, 5, ∞]
        #               ↑              ↑
        #             left           right  -> length = 4
        #   
        # [0, 1, 2, 3, 10, 4, 2, 3, 5, ∞]
        #           ↑            ↑
        #          left        right        -> length = 3
        #
        # [0, 1, 2, 3, 10, 4, 2, 3, 5, ∞]
        #        ↑            ↑
        #       left        right           -> length = 3
        #
        # [0, 1, 2, 3, 10, 4, 2, 3, 5, ∞]
        #        ↑            ↑
        #       left        right           -> length = 3
        #
        # [0, 1, 2, 3, 10, 4, 2, 3, 5, ∞]
        #     ↑               ↑
        #    left           right           -> length = 4
        #
        # [0, 1, 2, 3, 10, 4, 2, 3, 5, ∞]
        #  ↑                  ↑
        # left              right           -> length = 5
            
        return shortest
        