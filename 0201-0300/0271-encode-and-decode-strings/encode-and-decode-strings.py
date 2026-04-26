class Codec:
    def encode(self, strs: List[str]) -> str:
        return "\U0001f601".join(strs)

    def decode(self, s: str) -> List[str]:
        return s.split("\U0001f601")
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

class Codec2:
    def encode(self, strs):
        """
        Encodes a list of strings to a single string.

        :param strs: List of strings to encode.
        :return: Encoded string.
        """
        # Initialize an empty string to hold the encoded strings
        encoded_string = ''

        # Iterate over each string in the input list
        for s in strs:
            # Replace each occurrence of '/' with '//'
            # This is our way of "escaping" the slash character
            # Then add our delimiter '/:' to the end
            encoded_string += s.replace('/', '//') + '/:'

        # Return the final encoded string
        return encoded_string

    def decode(self, s):
        """
        Decodes a single string to a list of strings.

        :param s: String to decode.
        :return: List of decoded strings.
        """
        # Initialize an empty list to hold the decoded strings
        decoded_strings = []

        # Initialize a string to hold the current string being built
        current_string = ""

        # Initialize an index 'i' to start of the string
        i = 0

        # Iterate while 'i' is less than the length of the encoded string
        while i < len(s):
            # If we encounter the delimiter '/:'
            if s[i:i+2] == '/:':
                # Add the current_string to the list of decoded_strings
                decoded_strings.append(current_string)

                # Clear current_string for the next string
                current_string = ""

                # Move the index 2 steps forward to skip the delimiter
                i += 2

            # If we encounter an escaped slash '//'
            elif s[i:i+2] == '//':
                # Add a single slash to the current_string
                current_string += '/'

                # Move the index 2 steps forward to skip the escaped slash
                i += 2

            # Otherwise, just add the character to current_string
            else:
                current_string += s[i]
                i += 1

        # Return the list of decoded strings
        return decoded_strings

class Codec3:
    def encode(self, strs):
        # Initialize an empty string to hold the encoded string.
        encoded_string = ''
        for s in strs:
            # Append the length, the delimiter, and the string itself.
            encoded_string += str(len(s)) + '/:' + s
        return encoded_string

    def decode(self, s):
        # Initialize a list to hold the decoded strings.
        decoded_strings = []
        i = 0
        while i < len(s):
            # Find the delimiter.
            delim = s.find('/:', i)
            # Get the length, which is before the delimiter.
            length = int(s[i:delim])
            # Get the string, which is of 'length' length after the delimiter.
            str_ = s[delim+2 : delim+2+length]
            # Add the string to the list.
            decoded_strings.append(str_)
            # Move the index to the start of the next length.
            i = delim + 2 + length
        return decoded_strings