class FrequencyTracker:

    def __init__(self):
        #self.nums = [0] * (10**5 + 1) # frequency for the num
        #self.freq = [0] * (10**5 + 1) # count of nums with such freq
        self.nums = defaultdict(int)
        self.freq = defaultdict(int)

    def add(self, number: int) -> None:
        oldFreq = self.nums[number]
        if oldFreq > 0:
            self.freq[oldFreq] -= 1
        self.nums[number] += 1
        self.freq[oldFreq + 1] += 1

    def deleteOne(self, number: int) -> None:
        oldFreq = self.nums[number]
        if oldFreq == 0: return
        self.freq[oldFreq] -= 1
        self.nums[number] -= 1
        self.freq[oldFreq - 1] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)