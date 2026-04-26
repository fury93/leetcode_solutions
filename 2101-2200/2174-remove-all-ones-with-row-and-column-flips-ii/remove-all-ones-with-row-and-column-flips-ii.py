class Solution:
    def removeOnes(self, grid: List[List[int]]) -> int:
        num_rows, num_cols, seen, res = len(grid), len(grid[0]), set(), inf

        def backtrack(num_flips: int)-> None:
            nonlocal res, seen
            cells_of_one = [(row_idx, col_idx) for row_idx, col_idx in product(range(num_rows), range(num_cols)) if grid[row_idx][col_idx] and not {row_idx, col_idx+15} & seen]
            if not cells_of_one: res = min(res, num_flips)

            for row_idx, col_idx in cells_of_one:
                seen |= {row_idx, col_idx+15}
                backtrack(num_flips+1)
                seen -= {row_idx, col_idx+15}
            return

        backtrack(0)
        return res
        
class Solution2:
    def removeOnes(self, grid):
        m = len(grid)
        n = len(grid[0])
        self.ans = float('inf')
        self.flips = 0
        seen = set()
        def helper():
            flag = False
            for x in range(m):
                for y in range(n):
                    if grid[x][y] == 1 and ('r', x) not in seen and ('c', y) not in seen :
                        flag = True
                        seen.add(('r', x))
                        seen.add(('c', y))
                        self.flips+=1
                        helper()
                        self.flips-=1
                        seen.remove(('r', x))
                        seen.remove(('c', y))
                        
            if not flag:
                self.ans=min(self.ans, self.flips)
        
        helper()
        return self.ans