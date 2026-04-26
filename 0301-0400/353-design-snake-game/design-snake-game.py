class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.snake = deque([(0, 0)]) # head - left, tail - right, used for the order
        self.snakeCells = set((0, 0)) # use for fast search if current cell busy with the snake body
        self.food = deque((x, y) for x, y in food) # I prefere to use tuples for coordinats
        self.w = width
        self.h = height

    def move(self, direction: str) -> int:
        # 1. Make new move, it's new head position
        row, col = self.snake[0]
        match direction:
            case 'R': col += 1
            case 'L': col -= 1
            case 'U': row -= 1
            case 'D': row += 1

        # 2. Check if head doesn't go out of bounds (hits a wall)
        if not (0 <= row < self.h and 0 <= col < self.w): return -1 

        head = (row, col)
        # 3. If a food in the head cell => remove this food and leave old tail
        # 4. Else remove old tail, it will be moved to new head cell later
        if self.food and self.food[0] == head:
            self.food.popleft()
        else:
            self.snakeCells.discard(self.snake.pop())
        
        # 5. check if new head don't cross the snake body
        if head in self.snakeCells: return -1
        
        # 6. Add new head 
        self.snake.appendleft(head)
        self.snakeCells.add(head)

        # 7. Score equal to the snake size without the head
        return len(self.snake) - 1

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

class SnakeGame2:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.snake = collections.deque([(0,0)])    # snake head is at the front
        self.snake_set = {(0,0) : 1}
        self.width = width
        self.height = height
        self.food = food
        self.food_index = 0
        self.movement = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}
        

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        
        newHead = (self.snake[0][0] + self.movement[direction][0],
                   self.snake[0][1] + self.movement[direction][1])
        
        # Boundary conditions.
        crosses_boundary1 = newHead[0] < 0 or newHead[0] >= self.height
        crosses_boundary2 = newHead[1] < 0 or newHead[1] >= self.width
        
        # Checking if the snake bites itself.
        bites_itself = newHead in self.snake_set and newHead != self.snake[-1]
     
        # If any of the terminal conditions are satisfied, then we exit with rcode -1.
        if crosses_boundary1 or crosses_boundary2 or bites_itself:
            return -1

        # Note the food list could be empty at this point.
        next_food_item = self.food[self.food_index] if self.food_index < len(self.food) else None
        
        # If there's an available food item and it is on the cell occupied by the snake after the move, eat it
        if self.food_index < len(self.food) and \
            next_food_item[0] == newHead[0] and \
                next_food_item[1] == newHead[1]:  # eat food
            self.food_index += 1
        else:    # not eating food: delete tail                 
            tail = self.snake.pop()  
            del self.snake_set[tail]
            
        # A new head always gets added
        self.snake.appendleft(newHead)
        
        # Also add the head to the set
        self.snake_set[newHead] = 1

        return len(self.snake) - 1
        