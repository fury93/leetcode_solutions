class Solution:
    def grayCode(self, n: int):
        result = [0]
        isPresent = {0}
        self.grayCodeHelper(result, n, isPresent)
        return result

    def grayCodeHelper(self, result, n, isPresent):
        if len(result) == (1 << n):
            return True
        current = result[-1]
        for i in range(n):
            nextNum = current ^ (1 << i)
            if nextNum not in isPresent:
                isPresent.add(nextNum)
                result.append(nextNum)
                if self.grayCodeHelper(result, n, isPresent):
                    return True
                isPresent.remove(nextNum)
                result.pop()
        return False

class Solution2:
    def grayCode(self, n: int) -> List[int]:
        result = []
        self.grayCodeHelper(result, n)
        return result

    def grayCodeHelper(self, result: List[int], n: int):
        if n == 0:
            result.append(0)
            return
        # derive the n bits sequence from the (n - 1) bits sequence.
        self.grayCodeHelper(result, n - 1)
        currentSequenceLength = len(result)
        # Set the bit at position n - 1 (0 indexed) and assign it to mask.
        mask = 1 << (n - 1)
        for i in range(currentSequenceLength - 1, -1, -1):
            # mask is used to set the (n - 1)th bit from the LSB of all the numbers present in the current sequence.
            result.append(result[i] | mask)
        return

class Solution3:
    def grayCode(self, n):
        result = [0]
        for i in range(1, n + 1):
            previousSequenceLength = len(result)
            mask = 1 << (i - 1)
            for j in range(previousSequenceLength - 1, -1, -1):
                result.append(mask + result[j])
        return result

class Solution4:
    def __init__(self):
        self.nextNum = 0

    def grayCode(self, n):
        self.result = []
        self.grayCodeHelper(n)
        return self.result

    def grayCodeHelper(self, n):
        if n == 0:
            self.result.append(self.nextNum)
            return
        self.grayCodeHelper(n - 1)
        # Flip the bit at (n - 1)th position from right
        self.nextNum = self.nextNum ^ (1 << (n - 1))
        self.grayCodeHelper(n - 1)

class Solution5:
    def grayCode(self, n: int):
        result = []
        # there are 2 ^ n numbers in the Gray code sequence.
        sequenceLength = 1 << n
        for i in range(sequenceLength):
            num = i ^ i >> 1
            result.append(num)
        return result