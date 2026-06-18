class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # 1 hour = 360/12 = 30
        # 1 minute = 360 / 60 = 6
        # 60 min = 30 degree => 0.5 degree per minute
        h = hour % 12 * 30 + minutes * 0.5
        m = minutes * 6
        diff = abs(h-m)
        return diff if diff <= 180 else 360 - diff