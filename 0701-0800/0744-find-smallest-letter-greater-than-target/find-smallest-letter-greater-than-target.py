class Solution:
    def nextGreatestLetter2(self, letters: List[str], target: str) -> str:
        for l in letters:
            if l > target:
                return l
        return letters[0]

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters)-1
        
        if target < letters[0] or target >= letters[-1]:
            return letters[0]
        
        while l <=r:
            m = l + (r-l) //2
            if letters[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return letters[l]