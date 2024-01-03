'''
Description
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Example
Example1

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
Example2

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"
'''


class Solution:
    def encode(self, strs):
        # Initialize an empty string to store the encoded strings
        encoded_strs = ""

        # Iterate over each string in the input list
        for s in strs:
            # Add the length of the string, a "#" character, and the string itself to the encoded string
            encoded_strs += str(len(s)) + "#" + s
            print(f"Encoded string: {encoded_strs}")

        # Return the encoded string
        return encoded_strs

    def decode(self, encoded_str):
        # Initialize an empty list to store the decoded strings
        decoded_strs = []

        # Initialize a pointer to the start of the encoded string
        i = 0

        # Iterate over the encoded string
        while i < len(encoded_str):
            # Initialize a pointer to the "#" character
            j = i

            # Find the "#" character
            while encoded_str[j] != "#":
                j += 1

            # Get the length of the next string
            length = int(encoded_str[i:j])
            print(f"Length of next string: {length}")

            # Add the next string to the list of decoded strings
            decoded_strs.append(encoded_str[j + 1:j + length + 1])
            print(f"Decoded strings: {decoded_strs}")

            # Move the pointer to the start of the next string
            i = j + length + 1

        # Return the list of decoded strings
        return decoded_strs


sol = Solution()
print(sol.encode(["lint", "code", "love", "you"]))
print(sol.decode("4#lint4#code4#love3#you"))
print(sol.encode(["we", "say", ":", "yes"]))
print(sol.decode(["we", "say", ":", "yes"]))
