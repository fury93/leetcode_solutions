class Solution(object):
    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        def direction(a,b,c):
            return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
        d = None
        for i in range(1,len(points)):
            a = direction(points[i-2],points[i-1],points[i])
            if a == 0: continue
            if d == None: d = a
            else:
                if a*d < 0: return False
        if direction(points[-2],points[-1],points[0]) * d < 0:return False
        return True

def area(p,q,r):
    return (p[0]-r[0])*(q[1]-r[1])-(p[1]-r[1])*(q[0]-r[0])

class Solution2:
    def isConvex(self, points: List[List[int]]) -> bool:
        sign = 0
        for i in range(len(points)):
            a = area(points[i],points[i-1],points[i-2])
            if a:
                if not sign:
                    sign = 1 if a > 0 else -1
                elif a*sign < 1:
                    return False
        return True