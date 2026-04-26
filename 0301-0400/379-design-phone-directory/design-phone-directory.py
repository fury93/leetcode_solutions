class Phone:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.slots = [True] * maxNumbers # status of all phones slots, True -> is available
        self.phones = Phone(-1) # list of available phones
        prev = self.phones
        for i in range(maxNumbers):
            prev.next, prev = (cur:= Phone(i)), cur
        
    def get(self) -> int:
        if not self.phones.next: return -1
        bookPhone = self.phones.next
        self.phones.next = bookPhone.next
        self.slots[bookPhone.val] = False
        return bookPhone.val

    def check(self, number: int) -> bool:
        return self.slots[number]

    def release(self, number: int) -> None:
        if self.slots[number]: return # phone is free already
        self.slots[number] = True
        self.phones.next = Phone(number, self.phones.next)
        

class PhoneDirectory1:
    def __init__(self, max_numbers):
        # Queue to store all available slots.
        self.slots_available_queue = deque(range(max_numbers))

        # List to mark if a slot is available.
        self.is_slot_available = [True] * max_numbers
    
    def get(self):
        # If the queue is empty, it means no slot is available.
        if not self.slots_available_queue:
            return -1

        # Otherwise, get the first available slot from the queue,
        # mark that slot as not available and return the slot.
        slot = self.slots_available_queue.popleft()
        self.is_slot_available[slot] = False
        return slot
    
    def check(self, number):
        # Check if the slot at index 'number' is available or not.
        return self.is_slot_available[number]
    
    def release(self, number):
        # If the slot is already present in the queue, we don't do anything.
        if self.is_slot_available[number]:
            return

        # Otherwise, mark the slot 'number' as available.
        self.slots_available_queue.append(number)
        self.is_slot_available[number] = True

class PhoneDirectory2:
    def __init__(self, max_numbers):
        # Hash set to store all available slots.
        self.slots_available = set(range(max_numbers))

    def get(self):
        # If the hash set is empty it means no slot is available.
        if not self.slots_available:
            return -1

        # Otherwise, pop and return the first element from the hash set.
        return self.slots_available.pop()

    def check(self, number):
        # Check if the slot at index 'number' is available or not.
        return number in self.slots_available

    def release(self, number):
        # Mark the slot 'number' as available.
        self.slots_available.add(number)

class PhoneDirectory3:
    def __init__(self, maxNumbers):
        # List to mark if a slot is available.
        self.is_slot_available = [True] * maxNumbers

    def get(self):
        # Find an empty slot and return the respective index.
        index = next((i for i, available in enumerate(self.is_slot_available) if available), -1)
        if index != -1:
            self.is_slot_available[index] = False
        return index

    def check(self, number):
        # Check if the slot at index 'number' is available.
        return self.is_slot_available[number]

    def release(self, number):
        # Mark the slot at index 'number' as available.
        self.is_slot_available[number] = True

# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)