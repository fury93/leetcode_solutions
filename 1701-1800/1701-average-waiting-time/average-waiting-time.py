class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waitingTime, prevEnd = 0, 0
        for start, prepareTime in customers:
            prevEnd = max(prevEnd, start) + prepareTime
            waitingTime += prevEnd - start

        return waitingTime / len(customers)