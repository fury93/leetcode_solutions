class Solution:
    # x - minimum number of moves
    # x + (x-1) + (x-2) + ... + 1 => ariphmetic progression = x*(x+1)/2 >= n
    # x^2 + x - 2n = 0 (it's a quadratic equasion ax*2 + bx + c = 0)
    # D = b^2 - 4ac, x = (-b + sqrt(D)) / 2a - we need only positive root
    def twoEggDrop(self, n: int) -> int:
        # x = (-1 + math.sqrt(1^2 - 4 * (-2*n)))/2
        x = (-1 + math.sqrt(1 + 8*n))/2
        return math.ceil(x)