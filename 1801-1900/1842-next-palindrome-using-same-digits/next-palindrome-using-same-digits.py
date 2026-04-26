class Solution:
    def get_next_larger(self, sList):
        i = len(sList) - 2
        while i >= 0 and sList[i] >= sList[i + 1]:
            i -= 1
        if i < 0:
            return []

        j = len(sList) - 1
        while j>=0 and sList[i] >= sList[j]:
            j -= 1

        sList[i], sList[j] = sList[j], sList[i]
        sList[i + 1:] = reversed(sList[i + 1:])
        
        return sList
    
    def nextPalindrome(self, num: str) -> str:
        num_list = list(num)
        mid = len(num) // 2
        midStr = "" if (len(num) % 2 == 0) else num_list[mid]
        
        left_greater = self.get_next_larger(num_list[: mid])
        if not left_greater:
            return ""
        
        
        return  "".join(left_greater) + midStr + "".join(reversed(left_greater))
        