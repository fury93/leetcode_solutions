"""
logic:
1) What primitive should we use? Locks + Condition
2) We need a variable to keep track of the current green light direction.
3) A Lock is used to ensure that only one thread at a time can check and potentially change the light direction. 
This avoids race conditions.
4) We use a Condition to manage waiting and notifying cars when the light changes for their direction.

"""
import threading
class TrafficLight:
    def __init__(self):
        self.current_green = 1  # Start with the north-south direction (1 for north-south, 2 for east-west)
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)

    def carArrived(
        self,
        carId: int,                      # ID of the car
        roadId: int,                     # ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
        direction: int,                  # Direction of the car
        turnGreen: 'Callable[[], None]', # Use turnGreen() to turn light to green on current road
        crossCar: 'Callable[[], None]'   # Use crossCar() to make car cross the intersection
    ) -> None:
        with self.lock:
            # If the current light is not green for the car's direction, turn it green
            if self.current_green != roadId:
                self.current_green = roadId  # Change the green light direction
                turnGreen()  # Turn the light green for the current road

            # Wait until the car's road has the green light
            #while self.current_green != roadId:
            #    self.condition.wait()

            # Cross the car
            crossCar()

            # Notify other cars to check the condition if needed
            #self.condition.notify_all()
            
class TrafficLight2:
    def __init__(self):
        self.green = 1

    def carArrived(
        self,
        carId: int,                      # ID of the car
        roadId: int,                     # ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
        direction: int,                  # Direction of the car
        turnGreen: 'Callable[[], None]', # Use turnGreen() to turn light to green on current road
        crossCar: 'Callable[[], None]'   # Use crossCar() to make car cross the intersection
    ) -> None:
        if roadId != self.green: 
            turnGreen()
            self.green = roadId
        crossCar()