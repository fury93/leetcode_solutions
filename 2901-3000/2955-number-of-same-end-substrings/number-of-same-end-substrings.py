class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        res,  ln = [0] * len(queries), len(s)
        symbolFreq = [[0] * ln for _ in range(26)]
        for i, ch in enumerate(s):
            symbolFreq[ord(ch) - 97][i] = 1
        
        # generate prefix sum without initial 0 => [1,2,3,4] => [1,3,6,10]
        # itertools.accumulate(nums, initial=0) => [1,2,3,4] => [0, 1, 3, 6, 10]
        for freq in symbolFreq:
            for i in range(1, ln):
                freq[i] += freq[i-1]

        for i, (start, end) in enumerate(queries):
            allSubstrings = 0
            for freq in symbolFreq:
                freqEnd = freq[end]
                freqStart = 0 if start == 0 else freq[start-1]
                symbolCnt = freqEnd - freqStart
                if symbolCnt > 0:
                    allSubstrings += (symbolCnt * (symbolCnt + 1)) // 2

            res[i] = allSubstrings

        return res

class Solution1:
    def sameEndSubstringCount(
        self, s: str, queries: list[list[int]]
    ) -> list[int]:
        # Dictionary to store each character and its positions in the string 's'
        char_positions_map = {}

        # Traverse the string and store the index of each character in the dictionary
        for i, c in enumerate(s):
            if c not in char_positions_map:
                char_positions_map[c] = []
            char_positions_map[c].append(i)

        result = []

        # Process each query
        for left_index, right_index in queries:
            count_same_end_substrings = 0

            # For each unique character in the string, calculate the number of same-end substrings
            for positions in char_positions_map.values():
                # Get the number of occurrences of the character within the range [left_index, right_index]
                left_bound = bisect_left(positions, left_index)
                right_bound = bisect_right(positions, right_index)
                num_occurrences = right_bound - left_bound

                # Calculate the number of same-end substrings for this character
                count_same_end_substrings += (
                    num_occurrences * (num_occurrences + 1) // 2
                )

            # Store the result for this query
            result.append(count_same_end_substrings)

        return result

class Solution2:
    def sameEndSubstringCount(
        self, s: str, queries: List[List[int]]
    ) -> List[int]:
        n = len(s)
        # 2D list to store prefix sum of character frequencies for each character 'a' to 'z'
        char_freq_prefix_sum = [[0] * n for _ in range(26)]

        # Fill the frequency array
        for i, char in enumerate(s):
            char_freq_prefix_sum[ord(char) - ord("a")][i] += 1

        # Convert the frequency array into a prefix sum array
        for freq in char_freq_prefix_sum:
            for j in range(1, n):
                freq[j] += freq[j - 1]

        results = []

        # Process each query
        for left_index, right_index in queries:
            count_same_end_substrings = 0

            # For each character, calculate the frequency of occurrences within the query range
            for freq in char_freq_prefix_sum:
                left_freq = 0 if left_index == 0 else freq[left_index - 1]
                right_freq = freq[right_index]
                frequency_in_range = right_freq - left_freq

                # Calculate the number of same-end substrings for this character
                count_same_end_substrings += (
                    frequency_in_range * (frequency_in_range + 1) // 2
                )

            results.append(count_same_end_substrings)

        return results