class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        peekGarbageTime = endM = endP = endG = 0

        for i, g in reversed(list(enumerate(garbage))):
            peekGarbageTime += len(g)
            if not endM and 'M' in g: endM = i
            if not endP and 'P' in g: endP = i
            if not endG and 'G' in g: endG = i

        dist = list(accumulate(travel, initial = 0))

        return dist[endM] + dist[endP] + dist[endG] + peekGarbageTime