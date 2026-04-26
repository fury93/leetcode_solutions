class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        if not points: return True
        min_p=min([i[0] for i in points])
        max_p=max([i[0] for i in points])
        d=set()
        for i in points:
            d.add(tuple(i))
        for i in points:
            if (min_p+max_p-i[0], i[1]) not in d:
                return False
        return True

class Solution2:
    def isReflected(self, points: List[List[int]]) -> bool:
        if not points:
            return True
        point_set = set()
        # min_point = max_point = None
        x_mini, x_maxi = float('inf'), -float('inf')
        for x, y in points:
            point_set.add((x, y))
            if x < x_mini:
                x_mini = x
            if x > x_maxi:
                x_maxi = x

        
        sum_ = x_mini + x_maxi
        
        for x, y in points:
            # length = abs(line_x - x)
            # x_reflection = line_x + length if x < line_x else line_x - length
            if (sum_ - x, y) not in point_set:
                return False
            
        return True