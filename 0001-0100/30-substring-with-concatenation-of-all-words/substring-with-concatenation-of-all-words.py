class Solution:
    def findSubstring2(self, s: str, words: List[str]) -> List[int]:
        res, need, wlen, wcnt = [], Counter(words), len(words[0]), len(words)

        for i in range(len(s) - wlen * wcnt + 1):
            meet, meetcnt = Counter(), 0
            for j in range(wcnt):
                start = i + j * wlen
                word = s[start:start+wlen]
                if word not in need:
                    break
                
                meet[word] += 1
                meetcnt += 1
                if meet[word] > need[word]:
                   break
                   
                if meetcnt == wcnt:
                    res.append(i)

        return res

    """
	Time:   O(n*k), n = length of s, k = length of each word
	Memory: O(m*k), m = length of words, k = length of each word
	"""

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res, need, wlen, wcnt = [], Counter(words), len(words[0]), len(words)

        for i in range(wlen):
            meet, meetcnt, start = Counter(), 0, i
            for j in range(i, len(s) , wlen):
                word = s[j:j+wlen]
                
                if word not in need:
                    meetcnt, start = 0, j + wlen
                    meet.clear()
                    continue
                
                meet[word] += 1
                meetcnt += 1

                while meet[word] > need[word]:
                    meet[s[start:start+wlen]] -= 1
                    meetcnt -= 1
                    start += wlen

                if meetcnt == wcnt:
                    res.append(start)

        return res

class Solution1:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        k = len(words)
        word_length = len(words[0])
        substring_size = word_length * k
        word_count = collections.Counter(words)

        def check(i):
            # Copy the original dictionary to use for this index
            remaining = word_count.copy()
            words_used = 0

            # Each iteration will check for a match in words
            for j in range(i, i + substring_size, word_length):
                sub = s[j : j + word_length]
                if remaining[sub] > 0:
                    remaining[sub] -= 1
                    words_used += 1
                else:
                    break

            # Valid if we used all the words
            return words_used == k

        answer = []
        for i in range(n - substring_size + 1):
            if check(i):
                answer.append(i)

        return answer

class Solution2:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        k = len(words)
        word_length = len(words[0])
        substring_size = word_length * k
        word_count = collections.Counter(words)

        def sliding_window(left):
            words_found = collections.defaultdict(int)
            words_used = 0
            excess_word = False

            # Do the same iteration pattern as the previous approach - iterate
            # word_length at a time, and at each iteration we focus on one word
            for right in range(left, n, word_length):
                if right + word_length > n:
                    break

                sub = s[right : right + word_length]
                if sub not in word_count:
                    # Mismatched word - reset the window
                    words_found = collections.defaultdict(int)
                    words_used = 0
                    excess_word = False
                    left = right + word_length  # Retry at the next index
                else:
                    # If we reached max window size or have an excess word
                    while right - left == substring_size or excess_word:
                        # Move the left bound over continously
                        leftmost_word = s[left : left + word_length]
                        left += word_length
                        words_found[leftmost_word] -= 1

                        if (
                            words_found[leftmost_word]
                            == word_count[leftmost_word]
                        ):
                            # This word was the excess word
                            excess_word = False
                        else:
                            # Otherwise we actually needed it
                            words_used -= 1

                    # Keep track of how many times this word occurs in the window
                    words_found[sub] += 1
                    if words_found[sub] <= word_count[sub]:
                        words_used += 1
                    else:
                        # Found too many instances already
                        excess_word = True

                    if words_used == k and not excess_word:
                        # Found a valid substring
                        answer.append(left)

        answer = []
        for i in range(word_length):
            sliding_window(i)

        return answer