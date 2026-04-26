class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        return sorted([key for key, val in Counter(bulbs).items() if val & 1])