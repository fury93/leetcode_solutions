class Solution:
    def maxArea(self, height: int, positions: List[int], 
                      directions: str) -> int:

        n, u = len(directions), directions.count('U')
        ans = mx = sum(positions)
        vertices = defaultdict(int, {0:0})

        for dir, pos in zip(directions, positions):
            if dir == "U":
                vertices[height - pos]-= 1
                vertices[2*height - pos]+= 1
            else: #dir == "D":
                vertices[height + pos]-= 1
                vertices[pos]+= 1
                
        for left, rght in pairwise(sorted(vertices)):

            mx+= (rght - left) * (2*u-n)
            if mx > ans: ans = mx
            u+= vertices[rght]

        return ans