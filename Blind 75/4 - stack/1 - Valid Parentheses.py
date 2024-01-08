'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

'''


class Solution:
    def isValid(self, s: str) -> bool:
        # Define the mapping of closing brackets to opening brackets
        bracketMapping = {')': '(', ']': '[', '}': '{'}
        # Initialize an empty stack
        stack = []
        # Iterate over the string
        for char in s:
            # If the character is a closing bracket
            if char in bracketMapping:
                # If the stack is empty or the top of the stack is not the corresponding opening bracket, return False
                if not stack or bracketMapping[char] != stack.pop():
                    print(f"Invalid closing bracket: {char}")
                    return False
            # If the character is an opening bracket, push it onto the stack
            else:
                stack.append(char)
                print(f"Pushed opening bracket onto stack: {char}")
        # If the stack is empty, return True. Otherwise, return False
        return not stack


# example usage
sol = Solution()
s = "()"
print(sol.isValid(s))
s = "()[]{}"
print(sol.isValid(s))
s = "(]"
print(sol.isValid(s))
s = "([)]"
print(sol.isValid(s))
