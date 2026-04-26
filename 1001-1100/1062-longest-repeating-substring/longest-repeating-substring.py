class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        length = len(s)
        dp = [[0] * (length + 1) for _ in range(length + 1)]
        max_length = 0

        for i in range(1, length + 1):
            for j in range(i + 1, length + 1):
                if s[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_length = max(max_length, dp[i][j])
        return max_length


# Approach 3: Suffix Array with Sorting
class Solution3:
    def longestRepeatingSubstring(self, s: str) -> int:
        length = len(s)
        suffixes = []

        # Create suffix array by storing all suffixes of the string
        for i in range(length):
            suffixes.append(s[i:])
        # Sort the suffix array
        suffixes.sort()

        max_length = 0
        # Compare adjacent suffixes to find the longest common prefix
        for i in range(1, length):
            j = 0
            # Compare characters one by one until
            # they differ or end of one suffix is reached
            while (
                j < min(len(suffixes[i]), len(suffixes[i - 1]))
                and suffixes[i][j] == suffixes[i - 1][j]
            ):
                j += 1
            # Update max_length with the length of the common prefix
            max_length = max(max_length, j)
        return max_length

# Approach 4: Binary Search with Set
class Solution4:
    def longestRepeatingSubstring(self, s: str) -> int:
        start, end = 1, len(s) - 1

        while start <= end:
            mid = (start + end) // 2
            # Check if there's a repeating substring of length mid
            if self._has_repeating_substring(s, mid):
                start = mid + 1  # Try longer substrings
            else:
                end = mid - 1  # Try shorter substrings
        return start - 1

    def _has_repeating_substring(self, s: str, length: int) -> bool:
        seen_substrings = set()
        for i in range(len(s) - length + 1):
            # Extract a substring of the given length
            substring = s[i : i + length]
            # Check if the substring has been seen before
            if substring in seen_substrings:
                return True
            seen_substrings.add(substring)
        return False

# Approach 6: MSD Radix Sort
class Solution6:
    def longestRepeatingSubstring(self, s: str) -> int:
        length = len(s)
        suffixes = []

        # Create suffix array by storing all suffixes of the string
        for i in range(length):
            suffixes.append(s[i:])
        # Sort the suffix array using MSD Radix Sort
        self._msd_radix_sort(suffixes)

        max_length = 0
        # Compare adjacent suffixes to find the longest common prefix
        for i in range(1, length):
            j = 0
            # Compare characters one by one until they
            # differ or end of one suffix is reached

            while (
                j < min(len(suffixes[i]), len(suffixes[i - 1]))
                and suffixes[i][j] == suffixes[i - 1][j]
            ):
                j += 1
            # Update max_length with the length of the common prefix
            max_length = max(max_length, j)
        return max_length

    def _msd_radix_sort(self, input: List[str]) -> None:
        aux = ["" for _ in input]
        self._sort(input, 0, len(input) - 1, 0, aux)

    def _sort(
        self, input: List[str], lo: int, hi: int, depth: int, aux: List[str]
    ) -> None:
        if lo >= hi:
            return

        count = [0] * 28
        # Count frequencies of each character at the current depth
        for i in range(lo, hi + 1):
            count[self._char_at(input[i], depth) + 1] += 1

        # Compute cumulates which give positions of each character
        for i in range(1, 28):
            count[i] += count[i - 1]

        # Move items to auxiliary array based on cumulates
        for i in range(lo, hi + 1):
            aux[count[self._char_at(input[i], depth)]] = input[i]
            count[self._char_at(input[i], depth)] += 1

        # Copy back to original array
        for i in range(lo, hi + 1):
            input[i] = aux[i - lo]

        # Recursively sort for each character value
        for i in range(27):
            self._sort(
                input, lo + count[i], lo + count[i + 1] - 1, depth + 1, aux
            )

    def _char_at(self, s: str, index: int) -> int:
        if index >= len(s):
            return 0
        return ord(s[index]) - ord("a") + 1