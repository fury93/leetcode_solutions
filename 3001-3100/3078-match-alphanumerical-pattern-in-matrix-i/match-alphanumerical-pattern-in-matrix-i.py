from collections import defaultdict

class Solution(object):
    def findPattern(self, board, pattern):
        M, N = len(board), len(board[0])
        P, Q = len(pattern), len(pattern[0])

        def matches(r, c):
            # Dictionary to store character to digit mapping
            char_to_digit = {}
            digit_seen = set()
            
            for i in range(P):
                for j in range(Q):
                    p_char = pattern[i][j]
                    b_digit = board[r + i][c + j]
                    
                    if p_char.isdigit():
                        # Pattern has a digit; it must match the board digit
                        if int(p_char) != b_digit:
                            return False
                    else:
                        # Pattern has a letter
                        if p_char in char_to_digit:
                            # Ensure consistent mapping for this letter
                            if char_to_digit[p_char] != b_digit:
                                return False
                        else:
                            # Map letter to board digit, ensuring it's unique
                            if b_digit in digit_seen:
                                return False
                            char_to_digit[p_char] = b_digit
                            digit_seen.add(b_digit)
            return True

        # Iterate over all possible top-left corners of P x Q submatrices in board
        for r in range(M - P + 1):
            for c in range(N - Q + 1):
                if matches(r, c):
                    return [r, c]
        
        # If no match is found, return [-1, -1]
        return [-1, -1]