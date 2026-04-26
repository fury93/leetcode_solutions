class Solution:
    def minArea(self, image: List[List[str]], r: int, c: int) -> int:
        m, n = len(image), len(image[0])
        self.left = self.right = c
        self.top = self.bottom = r
        DIR = [0, 1, 0, -1, 0]
        
        def dfs(r, c):
            if r < 0 or r == m or c < 0 or c == n or image[r][c] == "0": return
            self.left = min(self.left, c)
            self.right = max(self.right, c)
            self.top = min(self.top, r)
            self.bottom = max(self.bottom, r)
            image[r][c] = "0"
            for i in range(4):
                dfs(r + DIR[i], c + DIR[i+1])
                
        dfs(r, c)
        return (self.bottom - self.top + 1) * (self.right - self.left + 1)

class Solution2:
    def minArea(self, image: List[List[str]], r: int, c: int) -> int:
        m, n = len(image), len(image[0])
        left = right = c
        top = bottom = r
        
        for r in range(m):
            for c in range(n):
                if image[r][c] == "0": continue
                left = min(left, c)
                right = max(right, c)
                top = min(top, r)
                bottom = max(bottom, r)
        return (bottom - top + 1) * (right - left + 1)

class Solution3:
    def minArea(self, image: List[List[str]], r: int, c: int) -> int:
        m, n = len(image), len(image[0])
        
        def existBlackPixelInCol(col):
            for r in range(m):
                if image[r][col] == "1":
                    return True
            return False
        
        def existBlackPixelInRow(row):
            return "1" in image[row]
        
        def searchMinCol(lo, hi):
            ans = hi
            while lo <= hi:
                mid = (lo + hi) // 2
                if existBlackPixelInCol(mid):
                    ans = mid
                    hi = mid - 1
                else:
                    lo = mid + 1
            return ans
        
        def searchMaxCol(lo, hi):
            ans = lo
            while lo <= hi:
                mid = (lo + hi) // 2
                if existBlackPixelInCol(mid):
                    ans = mid
                    lo = mid + 1
                else:
                    hi = mid - 1
            return ans
        
        def searchMinRow(lo, hi):
            ans = hi
            while lo <= hi:
                mid = (lo + hi) // 2
                if existBlackPixelInRow(mid):
                    ans = mid
                    hi = mid - 1
                else:
                    lo = mid + 1
            return ans
        
        def searchMaxRow(lo, hi):
            ans = lo
            while lo <= hi:
                mid = (lo + hi) // 2
                if existBlackPixelInRow(mid):
                    ans = mid
                    lo = mid + 1
                else:
                    hi = mid - 1
            return ans
        
        left = searchMinCol(0, c)
        right = searchMaxCol(c, n-1)
        top = searchMinRow(0, r)
        bottom = searchMaxRow(r, m-1)
        return (bottom - top + 1) * (right - left + 1)