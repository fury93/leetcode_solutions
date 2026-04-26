# Definition for a street.
# class Street:
#     def closeDoor(self):
#         pass
#     def isDoorOpen(self):
#         pass
#     def moveRight(self):
#         pass
class Solution:
    def houseCount(self, street: Optional['Street'], k: int) -> int:
        # No. of steps to reach the first open door
        x_first = 0

        # No. of steps from the current open door to the first open door.
        dist_from_first = 0

        # No. of steps in our traversal.
        x = 0

        # If we have found (and skipped) the first open door
        find_first = False

        while x <= 2 * k:
            # If the door is open
            if street.isDoorOpen(): 
                # If we have skipped the first door, update dist_from_first
                # and close the open door.
                if find_first:
                    dist_from_first = x - x_first
                    street.closeDoor()

                # Otherwise, we skip this open door and record its index as x_first = x.
                else:
                    x_first = x
                    find_first = True

            # Move to the next house on the right, and increase x by 1.
            street.moveRight()
            x += 1
        
        return dist_from_first
        
class Solution2:
    def houseCount(self, street: Optional['Street'], k: int) -> int:

        def period() -> int:
            pattern = []
            for _ in range(2*k):
                pattern.append(street.isDoorOpen())
                street.moveRight()

            # KMP algorithm
            kmp, ptr = [0], 0
            for i in range(1,2*k):
                while ptr and pattern[i] != pattern[ptr]:
                    ptr = kmp[ptr-1]
                if pattern[i] == pattern[ptr]:
                    ptr += 1
                kmp.append(ptr)

            # The shortest period is 2k minus the longest match at the end
            return 2*k - ptr

        prd1 = period()

        while not street.isDoorOpen():
            street.moveRight()
        street.closeDoor()

        prd2 = period()

        # Least common multiple
        return lcm(prd1, prd2)