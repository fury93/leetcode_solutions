class Solution:
    # Approach 3: QuickSelect
    def findKthLargest3(self, nums: List[int], k: int) -> int:
        if len(nums) == 1: return nums[0]

        def findKthLargest(nums, k):
            pivot = random.choice(nums)
            left = [n for n in nums if n > pivot]
            mid = [n for n in nums if n == pivot]
            right = [n for n in nums if n < pivot]
            
            L, M = len(left), len(mid)
            
            if k <= L:
                return findKthLargest(left, k) # midIndex not included like most right element
            elif k > L + M:
                return findKthLargest(right, k - L - M)
            else:
                return mid[0]

        return findKthLargest(nums, k)

    # Approach 4: Counting Sort O(N + M)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_value = min(nums)
        max_value = max(nums)
        count = [0] * (max_value - min_value + 1)

        for num in nums:
            count[num - min_value] += 1
        
        remain = k
        for num in range(len(count) -1, -1, -1):
            remain -= count[num]
            if remain <= 0:
                return num + min_value

        return -1

    # Approach 2: Min-Heap O(N*logK)
    def findKthLargest2(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]

    # Approach 1: Sort O(N*LogN)
    def findKthLargest1(self, nums, k):
        nums.sort(reverse=True)
        return nums[k - 1]