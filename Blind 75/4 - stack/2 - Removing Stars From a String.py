'''
You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.
 

Example 1:

Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".
Example 2:

Input: s = "erase*****"
Output: ""
Explanation: The entire string is removed, so we return an empty string.
 

'''


class Solution:
    def removeStars(self, star_string: str) -> str:
        """Removes all consecutive stars from a string.

        Args:
            star_string: The string containing stars.

        Returns:
            The string with all consecutive stars removed.
        """

        character_stack = []  # Stack to store characters
        character_stack.append(star_string[0])  # Push the first character

        for i in range(1, len(star_string)):
            current_char = star_string[i]

            if current_char != "*":
                character_stack.append(current_char)
                # print(f"Current stack: {character_stack}")
            else:
                if character_stack and character_stack[-1] != "*":
                    character_stack.append(current_char)
                    # print(f"Current stack: {character_stack}")

        return "".join(character_stack)  # Join characters in the stack
