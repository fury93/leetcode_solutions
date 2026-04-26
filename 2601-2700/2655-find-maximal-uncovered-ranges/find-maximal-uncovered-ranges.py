class Solution:
    def findMaximalUncoveredRanges(self, n: int, ranges: List[List[int]]) -> List[List[int]]:
        ranges.sort()
        res, missing_start = [], 0
        for start, end in ranges + [[n , n]]:
            if missing_start < start:
                res.append([missing_start, start-1])
            missing_start = max(missing_start, end + 1)
        return res 

    def findMaximalUncoveredRanges2(self, n: int, ranges: List[List[int]]) -> List[List[int]]:
        if not ranges: return [[0, n-1]]
        
        ranges.sort()
        merged_ranges = [ranges[0]]
        for i in range(1, len(ranges)):
            if merged_ranges[-1][1] >= ranges[i][0]:
                merged_ranges[-1][1] = max(merged_ranges[-1][1], ranges[i][1])
            else:
                merged_ranges.append(ranges[i])
          
        if merged_ranges[-1][1] != n:
            merged_ranges.append([n,n])

        res, missing_start = [], 0
        for start, end in merged_ranges:
            if missing_start != start:
                res.append([missing_start, start-1])
            missing_start = end + 1
        return res      