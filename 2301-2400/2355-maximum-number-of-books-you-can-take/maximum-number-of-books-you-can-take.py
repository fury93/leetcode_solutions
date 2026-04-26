class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        n = len(books)

        # Helper function to calculate the sum of books in a given range [l, r]
        def calculateSum(l, r):
            cnt = min(books[r], r - l + 1)
            return (2 * books[r] - (cnt - 1)) * cnt // 2

        stack = []
        dp = [0] * n

        for i in range(n):
            # While we cannot push i, we pop from the stack
            while stack and books[stack[-1]] - stack[-1] >= books[i] - i:
                stack.pop()

            # Compute dp[i]
            if not stack:
                dp[i] = calculateSum(0, i)
            else:
                j = stack[-1]
                dp[i] = dp[j] + calculateSum(j + 1, i)

            # Push the current index onto the stack
            stack.append(i)

        # Return the maximum element in the dp array
        return max(dp)
        
class Solution1:
    def maximumBooks(self, books: List[int]) -> int:
        res = 0
        stack = []
        for i in range(len(books)):
            while stack and books[i]<=books[stack[-1][0]]+(i-stack[-1][0]):
                stack.pop()
            prev_g_end,prev_g_res = stack[-1] if stack else [-1,0]
            h = min(i-prev_g_end,books[i])
            l1,l2 = books[i],books[i]-h+1
            cur = prev_g_res+(l1+l2)*h//2
            stack.append([i,cur])
            res = max(res,cur)
        return res

class Solution2:
    def maximumBooks(self, books: List[int]) -> int:
        n = len(books)
        dp, stack = [0] * n, []
        for i in range(n):
            if books[i] == 0:
                stack.append(i)
                continue
            while stack:
                j = stack[-1]
                if books[j] >= books[i] - (i - j):
                    stack.pop()
                else:
                    break
            if not stack:
                j = -1
            if books[i] - i + j + 1 < 0:
                dp[i] = books[i] * (books[i] + 1) // 2
            else:
                dp[i] = (books[i] + books[i] - i + j + 1) * (i - j) // 2
            if j >= 0:
                dp[i] += dp[j]
            stack.append(i)
        return max(dp)