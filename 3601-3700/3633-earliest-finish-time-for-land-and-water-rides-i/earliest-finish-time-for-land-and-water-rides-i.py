class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def findTime(s1, d1, s2, d2):
            finish = min(s + d for s, d in zip(s1, d1))
            return min(max(finish, s) + d for s, d in zip(s2, d2))

        return min(
            findTime(landStartTime, landDuration, waterStartTime, waterDuration),
            findTime(waterStartTime, waterDuration, landStartTime, landDuration),
        )
            

            



