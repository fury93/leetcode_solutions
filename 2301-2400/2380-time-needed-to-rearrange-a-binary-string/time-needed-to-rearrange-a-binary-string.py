class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        time, zeros = 0, 0
        # 1 0 0 1 1 => 1 0 1 0 1 => 1 1 0 1 0 => 1 1 1 0 0
        for n in s:
            if n == '0':
                zeros += 1
            elif zeros > 0:
                time = max(time + 1, zeros)

        return time
            



        