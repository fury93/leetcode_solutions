class Logger:

    def __init__(self):
        self.d = {}
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if timestamp < self.d.get(message, 0):
            return False
        self.d[message] = timestamp + 10
        return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)