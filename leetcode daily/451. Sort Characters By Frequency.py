'''
https://leetcode.com/problems/sort-characters-by-frequency/

451. Sort Characters By Frequency

Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

 

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
 

Constraints:

1 <= s.length <= 5 * 105
s consists of uppercase and lowercase English letters and digits.

'''


class Solution:
    def frequencySort(self, s: str) -> str:
        # Initialize an empty dictionary to store the frequency of each character
        character_frequency = {}
        print(f"Initial character frequency: {character_frequency}")

        # Iterate over each character in the string
        for character in s:
            # If the character is not in the dictionary, add it with a frequency of 1
            # If the character is in the dictionary, increment its frequency by 1
            character_frequency[character] = character_frequency.get(
                character, 0) + 1
            print(f"Updated character frequency: {character_frequency}")

        # Sort the items in the dictionary by their frequency in descending order
        sorted_character_frequency = sorted(
            character_frequency.items(), key=lambda x: x[1], reverse=True)
        print(f"Sorted character frequency: {sorted_character_frequency}")

        # Initialize an empty string to store the sorted characters
        sorted_string = ""

        # Iterate over each item in the sorted dictionary
        for character, frequency in sorted_character_frequency:
            # Append the character repeated by its frequency to the string
            sorted_string += character * frequency
            print(f"Updated sorted string: {sorted_string}")

        # Return the resulting string
        return sorted_string


class Solution:
    def frequencySort(self, s: str) -> str:
        # Initialize an empty dictionary to store the frequency of each character
        frequency_map = {}
        print(f"Initial frequency map: {frequency_map}")

        # Iterate over each character in the string
        for character in s:
            # If the character is not in the dictionary, add it with a frequency of 1
            # If the character is in the dictionary, increment its frequency by 1
            frequency_map[character] = frequency_map.get(character, 0) + 1
            print(f"Updated frequency map: {frequency_map}")

        # Sort the items in the dictionary by their frequency in descending order
        sorted_frequency_map = sorted(
            frequency_map.items(), key=lambda x: x[1], reverse=True)
        print(f"Sorted frequency map: {sorted_frequency_map}")

        # Create a list of strings where each string is a character repeated by its frequency
        sorted_characters = [
            character * frequency for character, frequency in sorted_frequency_map]
        print(f"Sorted characters: {sorted_characters}")

        # Join the list of strings into a single string
        result = ''.join(sorted_characters)
        print(f"Result: {result}")

        # Return the resulting string
        return result
