class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        students = [None] * 1001
        for idx, score in items:
            if not students[idx]: students[idx] = []
            if len(students[idx]) < 5:
                heappush(students[idx], score)
            else:
                heappushpop(students[idx], score)
               
        return [[key, sum(val)//5] for key, val in enumerate(students) if val]