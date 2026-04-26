class Solution:
    def nextClosestTime(self, time):
        cur = 60 * int(time[:2]) + int(time[3:])
        allowed = {int(x) for x in time if x != ':'}
        while True:
            cur = (cur + 1) % (24 * 60)
            if all(digit in allowed
                    for block in divmod(cur, 60)
                    for digit in divmod(block, 10)):
                return "{:02d}:{:02d}".format(*divmod(cur, 60))

class Solution2:
    def nextClosestTime(self, time):
        ans = start = 60 * int(time[:2]) + int(time[3:])
        elapsed = 24 * 60
        allowed = {int(x) for x in time if x != ':'}
        for h1, h2, m1, m2 in itertools.product(allowed, repeat = 4):
            hours, mins = 10 * h1 + h2, 10 * m1 + m2
            if hours < 24 and mins < 60:
                cur = hours * 60 + mins
                cand_elapsed = (cur - start) % (24 * 60)
                if 0 < cand_elapsed < elapsed:
                    ans = cur
                    elapsed = cand_elapsed

        return "{:02d}:{:02d}".format(*divmod(ans, 60))

# Doesn't work
class Solution_test:
    def nextClosestTime(self, time: str) -> str:
        digits = [time[0], time[1], time[3], time[4]]

        self.maxNum = 0
        def generate(digits, nums):
            if len(nums) == 4:
                curNum = int(''.join(nums))
                if curNum > self.maxNum and curNum < 2400:
                    self.maxNum = curNum
                return
            
            for i, d in enumerate(digits):
                nums.append(d)
                generate(digits, nums)
                nums.pop()

        generate(digits, [])

        maxTime = f'{self.maxNum // 100}:{self.maxNum % 100}'

        return maxTime


