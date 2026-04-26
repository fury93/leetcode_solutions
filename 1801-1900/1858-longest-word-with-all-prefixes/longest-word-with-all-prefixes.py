class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        longest_valid_word = ""

        # Insert all words into the trie
        for word in words:
            trie._insert(word)

        # Check each word and update the longest valid word
        for word in words:
            if trie._has_all_prefixes(word):
                if len(word) > len(longest_valid_word) or (
                    len(word) == len(longest_valid_word)
                    and word < longest_valid_word
                ):
                    longest_valid_word = word

        return longest_valid_word


class Trie:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_end_of_word = False

    def __init__(self):
        self.root = self.TrieNode()

    # Insert a word into the trie
    def _insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = self.TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    # Check if all prefixes of the word exist in the trie
    def _has_all_prefixes(self, word):
        node = self.root
        for char in word:
            if (
                char not in node.children
                or not node.children[char].is_end_of_word
            ):
                return False
            node = node.children[char]
        return True

class Solution2:
    def longestWord(self, words: List[str]) -> str:
        # Sort the words lexicographically
        words.sort()

        # Set to store valid words
        valid_words = set()
        longest_valid_word = ""

        # Iterate through each word
        for current_word in words:
            # Check if the word is of length 1 or if its prefix exists in the set
            if len(current_word) == 1 or current_word[:-1] in valid_words:
                # Add the current word to the set of valid words
                valid_words.add(current_word)

                # Update the longest valid word if necessary
                if len(current_word) > len(longest_valid_word):
                    longest_valid_word = current_word

        # Return the longest valid word found
        return longest_valid_word