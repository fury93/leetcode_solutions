class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        validCodes = {
            "electronics": [], "grocery": [], "pharmacy": [], "restaurant": []
        }

        def isValidCode(curCode):
            for char in curCode:
                if not (char.isalpha() or char.isdigit() or char == '_'):
                    return False
            return len(curCode) > 0

        for i in range(len(code)):
            if not isActive[i]: continue
            
            category = businessLine[i]
            if not category in validCodes.keys(): continue
            
            if isValidCode(code[i]):
                validCodes[category].append(code[i])

        return [c for cat in sorted(validCodes) for c in sorted(validCodes[cat])]
