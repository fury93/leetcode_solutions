class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda x: x[1])
        takenCourses = [] # max heap => return longest course
        curDay = 0

        for duration, lastDay in courses:
            heappush(takenCourses, -duration)
            curDay += duration
            if curDay > lastDay:
                curDay += heappop(takenCourses) # remove longest course

        return len(takenCourses)
