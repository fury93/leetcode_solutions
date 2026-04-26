class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for word_num in range(len(words)):
            for char_pos in range(len(words[word_num])):
                # char_pos (curr 'row' word) is bigger than column word, or
                # word_num (curr 'column' word) is bigger than row word, or 
                # characters at index (word_num,char_pos) and (char_pos,word_num) are not equal.
                if char_pos >= len(words) or \
                    word_num >= len(words[char_pos]) or \
                    words[word_num][char_pos] != words[char_pos][word_num]:
                    return False
        return True

# Approach 1: Storing New Words
class Solution1:
    def validWordSquare(self, words: List[str]) -> bool:
        cols = 0
        rows = len(words)
        new_words = []
        
        for word in words:
            cols = max(cols, len(word))

        # If the first row doesn't have maximum number of characters, or
        # the number of rows is not equal to columns it can't form a square.
        if cols != len(words[0]) or rows != cols:
            return False

        for col in range(cols):
            new_word = []
            # Iterate on each character of column 'col'.
            for row in range(rows):
                # If the current row's word's size is less than the column number it means this column is empty,
                # or, if there is a character present then use it to make the new word.
                if col < len(words[row]):
                    new_word.append(words[row][col])
            # Push the new word of column 'col' in the list.
            new_words.append(''.join(new_word))

        # Check if all row's words match with the respective column's words.
        return words == new_words

# Approach 2: Iterate on the Matrix
