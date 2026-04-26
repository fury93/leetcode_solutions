class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        # Increment k to account for 1-based indexing
        k = k + 1

        # Convert k to a binary string (up to the most significant '1')
        kth_lucky_num = bin(k)[3:]

        # Replace '0' with '4' and '1' with '7' in the binary string
        kth_lucky_num = kth_lucky_num.replace("0", "4").replace("1", "7")

        return kth_lucky_num

class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        return bin(k+1)[3:].replace('0','4').replace('1','7')

class Solution1:
    def kthLuckyNumber(self, k: int) -> str:
        c = 0  # The number of digits in the kth lucky number
        num_count = 0  # The number of lucky numbers with c or fewer digits
        while num_count < k:
            c += 1
            num_count += 2**c

        # Calculate the number of lucky numbers with c digits before the kth lucky number
        x = k - 1 - (num_count - (2**c))

        # Build result using x by prepending 4 for 0 and 1 for 7
        kth_lucky_num = ""
        for i in range(0, c):
            if x % 2 == 1:
                digit = "7"
            else:
                digit = "4"
            kth_lucky_num = "".join((digit, kth_lucky_num))
            x //= 2

        return kth_lucky_num

class Solution2:
    def kthLuckyNumber(self, k: int) -> str:
        # Increment k to account for 1-based indexing
        k = k + 1

        # For each digit in the binary representation of k except the most significant
        # Prepend 4 to the result if the digit is 0 and 7 otherwise
        kth_lucky_num = ""
        while k > 1:
            kth_lucky_num = "".join((("7" if k & 1 else "4"), kth_lucky_num))
            k >>= 1
        return kth_lucky_num