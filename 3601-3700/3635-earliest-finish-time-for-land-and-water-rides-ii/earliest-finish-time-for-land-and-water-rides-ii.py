class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        res = float("inf")
        time = float("inf")
        land, water = len(landStartTime), len(waterStartTime)

        for t, d in zip(landStartTime, landDuration):
            time = min(time, t + d)
        
        for i in range(water):
            if time < waterStartTime[i]:
                res = min(res, waterStartTime[i] + waterDuration[i])
            else:
                res = min(res, time + waterDuration[i])
        
        time = float("inf")
        for t, d in zip(waterStartTime, waterDuration):
            time = min(time, t + d)
        
        for i in range(land):
            if time < landStartTime[i]:
                res = min(res, landStartTime[i] + landDuration[i])
            else:
                res = min(res, time + landDuration[i])
        
        return res