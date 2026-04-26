class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(int(n[-4:-2]) > 60 for n in details)