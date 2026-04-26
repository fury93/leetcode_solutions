class Solution:
    def store_abbreviations(
        self, abbreviations, word, curr_word, index, abbreviated_count
    ):
        if index == len(word):
            # If the length of the last abbreviated substring is 0, add an empty string.
            if abbreviated_count > 0:
                curr_word += str(abbreviated_count)
            abbreviations.append(curr_word)
            return

        # Option 1: Keep the current character.
        self.store_abbreviations(
            abbreviations,
            word,
            curr_word
            + (str(abbreviated_count) if abbreviated_count > 0 else "")
            + word[index],
            index + 1,
            0,
        )

        # Option 2: Abbreviate the current character.
        self.store_abbreviations(
            abbreviations, word, curr_word, index + 1, abbreviated_count + 1
        )

    def generateAbbreviations(self, word):
        abbreviations = []
        self.store_abbreviations(abbreviations, word, "", 0, 0)
        return abbreviations

class Solution2:
    def generateAbbreviations(self, word):
        N = len(word)
        abbreviations = []

        for mask in range(1 << N):
            curr_word = []
            abbreviated_count = 0

            for index in range(N):
                # If the bit at the position index is 1, increment the abbreviated substring.
                if mask & (1 << index):
                    abbreviated_count += 1
                else:
                    # Append the last substring and then the current character.
                    if abbreviated_count > 0:
                        curr_word.append(str(abbreviated_count))
                        abbreviated_count = 0
                    curr_word.append(word[index])

            if abbreviated_count > 0:
                curr_word.append(str(abbreviated_count))

            abbreviations.append("".join(curr_word))

        return abbreviations