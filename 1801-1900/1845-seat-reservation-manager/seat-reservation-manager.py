class SeatManager:
    def __init__(self, n: int):
        self.lastBooked = 0
        self.unbooked = []

    def reserve(self) -> int:
        if self.unbooked: 
            return heappop(self.unbooked)
        self.lastBooked += 1
        return self.lastBooked

    def unreserve(self, seatNumber: int) -> None:
        if self.lastBooked == seatNumber:
            self.lastBooked -=1
        else:
            heappush(self.unbooked, seatNumber)