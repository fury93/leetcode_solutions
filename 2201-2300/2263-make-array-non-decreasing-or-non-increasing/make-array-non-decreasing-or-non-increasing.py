class Solution:
    def convertArray(self, nums: List[int]) -> int:
        res1 = 0
        min_heap = []
        for n in nums:
            if min_heap and min_heap[0] < n:
                res1 += n - heapq.heappop(min_heap)
                heapq.heappush(min_heap, n)
            heapq.heappush(min_heap, n)
        max_heap = []
        res2 = 0
        for n in nums:
            if max_heap and max_heap[0] < -n:
                res2 += - n - heapq.heappop(max_heap)
                heapq.heappush(max_heap, -n)

            heapq.heappush(max_heap, -n)
        return min(res1, res2)
        
        
class Solution2:
    def convertArray(self, nums: List[int]) -> int:
	
		### Some utilities. Should be easy to implement.
		
        def merge(arr_1, arr_2):
			# Just a merge sort.
			# Merge non-decreasing sequences arr_1 and arr_2 to a non-decreasing sequence
            answer = []
            
            len_1, len_2 = len(arr_1), len(arr_2);
            idx_1, idx_2 = 0, 0
            
            while idx_1 != len_1 and idx_2 != len_2:
                if arr_1[idx_1] <= arr_2[idx_2]:
                    answer.append(arr_1[idx_1])
                    idx_1 += 1
                else:
                    answer.append(arr_2[idx_2])
                    idx_2 += 1
                    
            return answer + arr_1[idx_1:] + arr_2[idx_2:]
        
        def median(arr):
			# Returns the median of the sorted sequence arr.
			# If arr has even length, return the smaller element.
            return arr[len(arr) // 2]

        def cost(arr):
			# Returns the cost to adjust all elements in sorted arr to its median
            med = median(arr)
            return sum(abs(x - med) for x in arr)
            
		### The main function. Does "half" of the problem.
		
        def non_dec(nums):
			# Find the minimal steps to change nums into an non-decreasing sequence
            stack = []
            
            for k in nums:
                arr = [k]
                while stack and median(stack[-1]) > median(arr):
                    arr = merge(arr, stack.pop())
                    
                stack.append(arr)
                
            return sum(cost(arr) for arr in stack)
        
		### To complete the task, we need to find the minimal of:
		### 1. Cost of changing num into a non-decreasing sequence; and
		### 2. Cost of changing num into a non-increasing sequence.
		### For 2, this can be done be reverting num and do 1. on num[::-1].
		
        return min(non_dec(nums), non_dec(nums[::-1]))