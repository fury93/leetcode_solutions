class Solution:
    # Stack
    def clearDigits2(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch.isalpha():
                stack.append(ch)
            elif stack:
                stack.pop()

        return ''.join(stack)

    # Two pointers
    def clearDigits(self, s: str) -> str:
        l, chars = 0, list(s)
        for r, ch in enumerate(chars):
            if ch.isalpha():
                chars[l] = ch
                l += 1
            else:
                l -= 1

        return ''.join(chars[:l])