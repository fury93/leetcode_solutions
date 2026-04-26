class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return reduce(lambda a, b: a + (1 if b[1] == '+' else -1) , operations, 0)