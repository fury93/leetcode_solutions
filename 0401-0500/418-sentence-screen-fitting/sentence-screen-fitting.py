class Solution:
    def wordsTyping(self, sentence, rows, cols):
        s = ' '.join(sentence) + ' '
        start = 0
        for i in range(rows):
            start += cols - 1
            if s[start % len(s)] == ' ':
                start += 1
            elif s[(start + 1) % len(s)] == ' ':
                start += 2
            else:
                while start > 0 and s[ (start - 1) % len(s) ] != ' ':
                    start -= 1
        return start // len(s)

class Solution2:
    def wordsTyping(self, s: List[str], rows: int, cols: int) -> int:
        n = len(s)
        jump,full = [],[]
        j = l = 0
        for i in range(n):
            full.append(full[-1] if i else 0)
            while l+len(s[j%n])+j-i <= cols:
                l += len(s[j%n])
                j += 1
                if not j%n:
                    full[-1] += 1
            jump.append(j%n)
            l -= len(s[i])
        i = count = k = 0
        while k < rows:
            count += full[i]
            i = jump[i]
            k += 1
            if i == 0 and rows >= 2*k:
                count *= rows//k
                k += k*(rows//k-1)
        return count

class Solution3:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        n = len(sentence)
        sentence_str = ' '.join(sentence) + ' '
        length = len(sentence_str)
        pos = 0
        
        for _ in range(rows):
            pos += cols
            
            # If we're in the middle of a word, move back to the beginning of the word
            while sentence_str[pos % length] != ' ':
                pos -= 1
            
            pos += 1

        return pos // length