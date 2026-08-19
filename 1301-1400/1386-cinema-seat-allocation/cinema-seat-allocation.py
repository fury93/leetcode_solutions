class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = defaultdict(set)

        for row, seat in reservedSeats:
            if seat in [2, 3, 4, 5]:
                seats[row].add(0)
            if seat in [4, 5, 6, 7]:
                seats[row].add(1)
            if seat in [6, 7, 8, 9]:
                seats[row].add(2)

        res = 2 * n
        for i in seats:
            if len(seats[i]) == 3:
                res -= 2
            else:
                res -= 1

        return res
        
    def maxNumberOfFamilies2(
        self, n: int, reservedSeats: List[List[int]]
    ) -> int:
        left, middle, right = 0b11110000, 0b11000011, 0b00001111
        occupied = collections.defaultdict(int)
        for seat in reservedSeats:
            if 2 <= seat[1] <= 9:
                occupied[seat[0]] |= 1 << (seat[1] - 2)

        ans = (n - len(occupied)) * 2
        for row, bitmask in occupied.items():
            if (
                (bitmask | left) == left
                or (bitmask | middle) == middle
                or (bitmask | right) == right
            ):
                ans += 1
        return ans