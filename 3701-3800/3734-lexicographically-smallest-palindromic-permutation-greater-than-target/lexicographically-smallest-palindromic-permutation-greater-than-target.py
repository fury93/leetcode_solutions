class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n, cnt = len(s), Counter(s)
        odds = [c for c, v in cnt.items() if v % 2]
        if len(odds) > n % 2:
            return ""

        mid, h = (odds[0] if odds else ""), n // 2
        pool = Counter({c: v // 2 for c, v in cnt.items()})
        build = lambda half: half + mid + half[::-1]

        stop = 0                                     # longest prefix of target[:h] the pool can match
        while stop < h and pool[target[stop]]:
            pool[target[stop]] -= 1
            stop += 1

        if stop == h and (p := build(target[:h])) > target:
            return p                                 # half forced -> exactly one candidate

        for i in range(stop, -1, -1):                # walk back to the last raisable position
            if i < h and (c := min((x for x in pool if x > target[i] and pool[x]), default="")):
                pool[c] -= 1
                return build(target[:i] + c + "".join(c * pool[c] for c in sorted(pool)))
            if i:
                pool[target[i - 1]] += 1             # un-consume, restoring the pool for i-1

        return ""
        
    def lexPalindromicPermutation2(self, s: str, target: str) -> str:
        n = len(s)
        # Special case: length of 1
        if n == 1:
            return s if s > target else ""

        # Count the frequency of each character
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord("a")] += 1

        # Check if it can form a palindrome and record the characters with odd occurrences
        odd_char = ""
        for i in range(26):
            if cnt[i] % 2 == 1:
                # More than one character appears an odd number of times, cannot form a palindrome
                if odd_char != "":
                    return ""
                odd_char = chr(ord("a") + i)
            cnt[
                i
            ] //= 2  # It takes only half the characters to construct the left half

        prefix = []

        def check(c):
            left = prefix.copy()
            left.append(c)
            for i in range(25, -1, -1):
                left.extend([chr(ord("a") + i)] * cnt[i])

            palindrome = left + [odd_char] + left[::-1]

            return "".join(palindrome) > target

        # Construct the left part of each digit greedily
        for i in range(n // 2):
            found = False
            # Try to place the smallest character in lexicographical order
            for j in range(26):
                if cnt[j] == 0:
                    continue

                cnt[j] -= 1
                if check(chr(ord("a") + j)):
                    # If the constructed palindrome is greater than target, choose the character
                    prefix.append(chr(ord("a") + j))
                    found = True
                    break
                else:
                    cnt[j] += 1  # Not meeting the conditions, reset the counter
            if not found:
                return ""  # Cannot construct a palindrome larger than target

            if prefix[i] > target[i]:  # prefix is already greater than target
                left = prefix[:]
                for j in range(26):
                    left.extend([chr(ord("a") + j)] * cnt[j])
                palindrome = left + [odd_char] + left[::-1]
                return "".join(palindrome)

        # Construct the final palindrome string
        ans = prefix + [odd_char] + prefix[::-1]
        return "".join(ans)