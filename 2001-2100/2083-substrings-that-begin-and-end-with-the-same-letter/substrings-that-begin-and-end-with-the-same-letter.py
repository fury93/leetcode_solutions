class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        return sum(n * (n+1) // 2 for n in Counter(s).values())

class Solution1:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        answer = 0
        prefix_count = [0] * 26

        for i in range(len(s)):
            # Increment the number of times we encountered the current letter so far.
            prefix_count[ord(s[i]) - ord("a")] += 1

            # Current letter can be paired with all the occurrences of it that
            # comes before, including itself, to form a valid substring.
            answer += prefix_count[ord(s[i]) - ord("a")]

        return answer

class Solution2:
    def numberOfSubstrings(self, s: str) -> int:
        answer = 0
        frequency_count = [0] * 26

        # Count the frequency of each character in the string.
        for ch in s:
            frequency_count[ord(ch) - ord("a")] += 1

        # Calculate the total number of valid substrings.
        for current_count in frequency_count:
            # Using (current_count + 1) choose 2 to calculate valid substrings
            # for the current letter.
            answer += ((current_count + 1) * current_count) // 2

        return answer