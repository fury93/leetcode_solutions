# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        def dfs(node, arr):
            if not node:
                return
            
            arr.append(node.val)
            dfs(node.left, arr)
            dfs(node.right, arr)
        
        arr = []
        dfs(root, arr)
        
        arr.sort(key = lambda x: (abs(x - target), x))
        return arr[:k]

class Solution2:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        def dfs(node, heap):
            if not node:
                return

            if len(heap) < k:
                heappush(heap, (-abs(node.val - target), node.val))
            else:
                if abs(node.val - target) <= abs(heap[0][0]):
                    heappop(heap)
                    heappush(heap, (-abs(node.val - target), node.val))

            dfs(node.left, heap)
            dfs(node.right, heap)

        heap = []
        dfs(root, heap)
        return [x[1] for x in heap]

class Solution3:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        def dfs(node, arr):
            if not node:
                return
            
            dfs(node.left, arr)
            arr.append(node.val)
            dfs(node.right, arr)
        
        arr = []
        dfs(root, arr)
        
        left = bisect_left(arr, target) - 1
        right = left + 1
        ans = []
        
        while len(ans) < k:
            if right == len(arr) or abs(arr[left] - target) <= abs(arr[right] - target):
                ans.append(arr[left])
                left -= 1
            else:
                ans.append(arr[right])
                right += 1
        
        return ans

class Solution4:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        def dfs(node, arr):
            if not node:
                return
            
            dfs(node.left, arr)
            arr.append(node.val)
            dfs(node.right, arr)
        
        arr = []
        dfs(root, arr)
        
        left = 0
        right = len(arr) - k
        
        while left < right:
            mid = (left + right) // 2
            if abs(target - arr[mid + k]) < abs(target - arr[mid]):
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]

class Solution5:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        def dfs(node, queue):
            if not node:
                return
            
            dfs(node.left, queue)
            queue.append(node.val)
            if len(queue) > k:
                if (abs(target - queue[0]) <= abs(target - queue[-1])):
                    queue.pop()
                    return
                else:
                    queue.popleft()
                    
            dfs(node.right, queue)
        
        queue = deque()
        dfs(root, queue)
        return queue