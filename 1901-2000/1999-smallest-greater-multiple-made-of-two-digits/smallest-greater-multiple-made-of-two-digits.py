class Solution:
    def findInteger(self, k: int, digit1: int, digit2: int) -> int:
        mn, mx = min(digit1, digit2), max(digit1, digit2)
        q = deque([])
        if mn != 0: q.append(mn)
        if mx != mn: q.append(mx)

        while q:
            num = q.popleft()
            if num > 2 ** 31 - 1:
                break
            if num > k and num % k == 0:
                return num
            q.append(num * 10 + mn)
            if mn != mx: q.append(num * 10 + mx)
        return -1