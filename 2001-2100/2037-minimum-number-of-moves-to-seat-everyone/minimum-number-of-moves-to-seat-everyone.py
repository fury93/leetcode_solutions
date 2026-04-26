class Solution:
    def minMovesToSeat2(self, seats: List[int], students: List[int]) -> int:
        res = 0
        for seat, student in zip(sorted(seats), sorted(students)):
            res += abs(seat - student)
        return res

    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        max_position = max(max(seats), max(students))
        differences = [0] * (max_position)

        # Count the available seats at each position
        for position in seats:
            differences[position - 1] += 1

        # Remove a seat for each student at that position
        for position in students:
            differences[position - 1] -= 1

        moves = 0
        unmatched = 0
        for difference in differences:
            moves += abs(unmatched)
            unmatched += difference

        return moves