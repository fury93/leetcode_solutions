class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        return sum(i * j for i, j in zip(sorted(nums1), sorted(nums2, reverse=True)))
        
class Solution1:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        # Sort nums1 in ascending order, and nums2 in
        # descending order.
        nums1.sort()
        nums2.sort(reverse=True)
        
        # Initialize sum as 0.
        ans = 0
        
        # Iterate over two sorted arrays and calculate the 
        # cumulative product sum. 
        for num1, num2 in zip(nums1, nums2):
            ans += num1 * num2

        return ans

class Solution2:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        # Sort nums1 in ascending order.
        nums1.sort()

        # Initialize a PriorityQueue pq as a Max-Heap, and add 
        # every element of nums2 to pq. 
        pq = [-num for num in nums2]       
        heapq.heapify(pq)
        
        # Initialize the product sum as 0 before the iteration.
        ans = 0

        # During the iteration
        for idx in range(len(nums2)):  
            # Add the product of nums[idx] and the maximum element
            # left in pq, remove this element from pq
            ans += nums1[idx] * (-heapq.heappop(pq))

        return ans

class Solution3:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        # Initialize counter1 and counter2.
        counter1, counter2 = [0] * 101, [0] * 101

        # Record the number of occurrence of elements in nums1 and nums2.
        for num in nums1:
            counter1[num] += 1
        for num in nums2:
            counter2[num] += 1
        
        # Initialize two pointers p1 = 1, p2 = 100.
        # Stands for counter1[1] and counter2[100], respectively.
        p1, p2 = 1, 100
        ans = 0
        
        # While the two pointers are in the valid range.
        while p1 <= 100 and p2 > 0:

            # If counter1[p1] == 0, meaning there is no element equals p1 in counter1,
            # thus we shall increment p1 by 1.
            while p1 <= 100 and counter1[p1] == 0:
                p1 += 1

            # If counter2[p2] == 0, meaning there is no element equals p2 in counter2,
            # thus we shall decrement p2 by 1.
            while p2 > 0 and counter2[p2] == 0:
                p2 -= 1

            # If any of the pointer goes beyond the border, we have finished the 
            # iteration, break the loop.
            if p1 == 101 or p2 == 0:
                break

            # Otherwise, we can make at most min(counter1[p1], counter2[p2]) 
            # pairs {p1, p2} from nums1 and nums2, let's call it occ. 
            # Each pair has product of p1 * p2, thus the cumulative sum is 
            # incresed by occ * p1 * p2. Update counter1[p1] and counter2[p2].
            occ = min(counter1[p1], counter2[p2])
            ans += occ * p1 * p2
            counter1[p1] -= occ
            counter2[p2] -= occ
        
        # Once we finish the loop, return ans as the product sum.
        return ans       