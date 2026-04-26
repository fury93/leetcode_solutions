class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        volume = sum(apple)
        for i, boxCapacity in enumerate(sorted(capacity, reverse= True), start=1):
            volume -= boxCapacity
            if volume <= 0: break
        return i