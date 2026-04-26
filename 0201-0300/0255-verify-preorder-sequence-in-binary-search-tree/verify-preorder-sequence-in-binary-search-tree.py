class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        min_limit = -math.inf
        stack = []
        
        for num in preorder:
            while stack and stack[-1] < num:
                min_limit = stack.pop()
                
            if num <= min_limit:
                return False
            
            stack.append(num)
        
        return True

class Solution2:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        min_limit = -inf
        i = 0
        
        for num in preorder:
            while i > 0 and preorder[i - 1] < num:
                min_limit = preorder[i - 1]
                i -= 1
                
            if num <= min_limit:
                return False
            
            preorder[i] = num
            i += 1
        
        return True

class Solution3:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        def helper(i, min_limit, max_limit):
            if i[0] == len(preorder):
                return True
            
            root = preorder[i[0]]
            if not min_limit < root < max_limit:
                return False

            i[0] += 1
            left = helper(i, min_limit, root)
            right = helper(i, root, max_limit)
            return left or right
            
        return helper([0], -inf, inf)