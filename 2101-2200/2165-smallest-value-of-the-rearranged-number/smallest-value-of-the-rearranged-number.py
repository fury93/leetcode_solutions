class Solution:
    # chatGpt
    def smallestNumber(self, num: int) -> int:
        # Convert the number to a string and determine if it's negative
        is_negative = num < 0
        num_str = str(abs(num))
        
        # Create a list of digits
        digits = list(num_str)
        
        if is_negative:
            # For negative numbers, sort in descending order
            digits.sort(reverse=True)
        else:
            # For positive numbers, sort in ascending order
            digits.sort()
            
            # Move the first non-zero digit to the front if there is a zero
            if digits[0] == '0':
                for i in range(1, len(digits)):
                    if digits[i] != '0':
                        # Swap the first non-zero with the first digit
                        digits[0], digits[i] = digits[i], digits[0]
                        break
        
        # Join the sorted digits back to form the result
        result_str = ''.join(digits)
        
        # Convert back to integer and adjust sign
        result = int(result_str)
        return result if not is_negative else -result
    
    # My solution
    def smallestNumber2(self, num: int) -> int:
        if num == 0: return num
        isNegative =  num < 0
        num = abs(num)
        digits, zeros = [], 0
        for n in str(num):
            if n == '0':
                zeros += 1
            else:
                digits.append(n)
        
        digits.sort(reverse = isNegative)

        if not isNegative:
            res = digits[0] + '0' * zeros + ''.join(digits[1:])
        else:
            res = '-' + ''.join(digits) + '0' * zeros
        
        return int(res)
