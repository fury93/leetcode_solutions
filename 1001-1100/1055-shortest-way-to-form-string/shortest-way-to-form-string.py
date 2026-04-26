class Solution:
    def shortestWay(self, source: str, target: str) -> int:

        # To check if to_check is subsequence of in_string
        def is_subsequence(to_check, in_string):
            i = j = 0
            while i < len(to_check) and j < len(in_string):
                if to_check[i] == in_string[j]:
                    i += 1
                j += 1

            return i == len(to_check)

        # Set of all characters of the source. We could use a boolean array as well.
        source_chars = set(source)

        # Check if all characters of the target are present in the source
        # If any character is not present, return -1
        for char in target:
            if char not in source_chars:
                return -1

        # Concatenate source until the target is a subsequence
        # of the concatenated string
        concatenated_source = source
        count = 1
        while not is_subsequence(target, concatenated_source):
            concatenated_source += source
            count += 1

        # Number of concatenations done
        return count

class Solution3:
    def shortestWay(self, source: str, target: str) -> int:

        # Set of all characters of source. Can use a boolean array too.
        source_chars = set(source)

        # Check if all characters of target are present in source
        # If any character is not present, return -1
        for char in target:
            if char not in source_chars:
                return -1

        # Length of source to loop back to start of source using mod
        m = len(source)

        # Pointer for source
        source_iterator = 0

        # Number of times source is traversed. It will be incremented when
        # while finding the occurrence of a character in target, source_iterator
        # reaches the start of source again.
        count = 0

        # Find all characters of target in source
        for char in target:

            # If while finding, iterator reaches start of source again,
            # increment count
            if source_iterator == 0:
                count += 1

            # Find the first occurrence of char in source
            while source[source_iterator] != char:

                # Formula for incrementing while looping back to start.
                source_iterator = (source_iterator + 1) % m

                # If while finding, iterator reaches the start of source again,
                # increment count
                if source_iterator == 0:
                    count += 1

            # Loop will break when char is found in source. Thus, increment.
            # Don't increment count until it is not clear that target has
            # remaining characters.
            source_iterator = (source_iterator + 1) % m

        # Return count
        return count

class Solution4:
    def shortestWay(self, source: str, target: str) -> int:

        # List of indices for all characters in source
        char_to_indices = defaultdict(list)
        for i, c in enumerate(source):
            char_to_indices[c].append(i)

        # Pointer for source
        source_iterator = 0

        # Number of times we need to iterate through source
        count = 1

        # Find all characters of target in source
        for char in target:

            # If character is not in source, return -1
            if char not in char_to_indices:
                return -1

            # Binary Search to find the index of the character in source
            # next to the current source_iterator
            index = bisect.bisect_left(char_to_indices[char], source_iterator)

            # If we have reached the end of the list, we need to iterate
            # through source again, hence first index of character in source.
            if index == len(char_to_indices[char]):
                count += 1
                source_iterator = char_to_indices[char][0] + 1
            else:
                source_iterator = char_to_indices[char][index] + 1

        # Return the number of times we need to iterate through source
        return count

class Solution5:
    def shortestWay(self, source: str, target: str) -> int:

        # Length of source
        source_length = len(source)

        # Next Occurrence of Character after Index
        next_occurrence = [defaultdict(int) for idx in range(source_length)]

        # Base Case
        next_occurrence[source_length -
                        1][source[source_length - 1]] = source_length - 1

        # Using Recurrence Relation to fill next_occurrence
        for idx in range(source_length - 2, -1, -1):
            next_occurrence[idx] = next_occurrence[idx + 1].copy()
            next_occurrence[idx][source[idx]] = idx

        # Pointer for source
        source_iterator = 0

        # Number of times we need to iterate through source
        count = 1

        # Find all characters of target in source
        for char in target:

            # If character is not in source, return -1
            if char not in next_occurrence[0]:
                return -1

            # If we have reached the end of source, or the character is not in
            # source after source_iterator, loop back to beginning
            if (source_iterator == source_length or
                    char not in next_occurrence[source_iterator]):
                count += 1
                source_iterator = 0

            # Next occurrence of character in source after source_iterator
            source_iterator = next_occurrence[source_iterator][char] + 1

        # Return the number of times we need to iterate through source
        return count