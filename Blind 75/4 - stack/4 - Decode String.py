'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 
'''


'''
 **Here's the rewritten code with explanations, intuition, approach, pseudo code, and complexity:**

**# Intuition**

- **Key idea:** Use a stack to manage nested patterns and reverse the order of characters for correct decoding.
- **Stack handling:** Push characters and substrings onto the stack, and pop them when decoding is needed.

**# Approach**

1. **Initialize a stack to store characters and substrings.**
2. **Iterate through each character in the input string:**
   - **If the character is not a closing bracket "]":**
     - Push it onto the stack.
   - **If the character is a closing bracket "]":**
     - **Decode the pattern:**
       - Pop characters from the stack until an opening bracket "[":
         - Reverse them to form the encoded substring.
       - Pop the opening bracket "[":
       - Pop digits from the stack to form the multiplier.
       - Expand the pattern by multiplying the substring by the multiplier.
       - Push the expanded string back onto the stack.
3. **Join the remaining characters in the stack to form the decoded string.**
4. **Return the decoded string.**

**# Pseudo Code**

```
1. Initialize stack = []
2. For each character in input string:
    a. If character is not "]":
        - Push character onto stack
    b. Else if character is "]":
        - Pop characters from stack until "[" is found, reverse them to form substring
        - Pop "[" from stack
        - Pop digits from stack to form multiplier
        - Push multiplied substring onto stack
3. Return joined characters in stack
```

**# Complexity**

- **Time complexity:** O(n), where n is the length of the input string. Each character is processed at most twice (once in the main loop and potentially once in the decoding loop).
- **Space complexity:** O(n), due to the stack potentially holding all characters in the worst case.

**# Code with Debugging Print Statements and Comments**

```python []
class Solution:
    def decodeString(self, encoded_string: str) -> str:
        decoding_stack = []  # Initialize stack for decoding

        for char in encoded_string:
            print(f"Processing character: {char}")

            if char != "]":
                decoding_stack.append(char)
                print(f"Pushed {char} onto stack")
            else:
                # Decode the pattern upon encountering a closing bracket
                encoded_substring = ""
                while decoding_stack and decoding_stack[-1] != "[":
                    encoded_substring = decoding_stack.pop() + encoded_substring
                print(f"Decoded substring: {encoded_substring}")

                decoding_stack.pop()  # Remove opening bracket "["

                multiplier_string = ""
                while decoding_stack and decoding_stack[-1].isdigit():
                    multiplier_string = decoding_stack.pop() + multiplier_string
                print(f"Multiplier: {multiplier_string}")

                multiplier = int(multiplier_string)
                expanded_string = multiplier * encoded_substring
                print(f"Expanded string: {expanded_string}")

                decoding_stack.append(expanded_string)
                print(f"Pushed expanded string onto stack")

        return "".join(decoding_stack)
```
```python []
class Solution:
    def decodeString(self, s: str) -> str:

        # Intuition
        # We can use a recursive approach to process the string and build the decoded result.
        # At each step, we handle digits, opening brackets, closing brackets, and characters.

        # Approach
        # We define a recursive function 'recurse' that takes the input string and the current position as parameters.
        # The function processes the string character by character, handling digits, brackets, and characters accordingly.
        # We use a while loop to iterate through the string and accumulate the decoded result.

        # Pseudo Code
        # def recurse(s, pos):
        #     result = ""
        #     i, num = pos, 0
        #     while i < len(s):
        #         c = s[i]
        #         if c.isdigit():
        #             num = num * 10 + int(c)
        #         elif c == '[':
        #             string, end = recurse(s, i + 1)
        #             result += num * string
        #             i = end
        #             num = 0
        #         elif c == ']':
        #             return result, i
        #         else:
        #             result += c
        #         i += 1
        #     return result, i
        #
        # We initiate the recursion with recurse(s, 0) and return the decoded result.

        def recurse(s, pos):
            result = ""
            i, num = pos, 0

            while i < len(s):
                c = s[i]
                print(f"Processing character: {c}")

                if c.isdigit():
                    num = num * 10 + int(c)
                elif c == '[':
                    print("Found opening bracket '['")
                    string, end = recurse(s, i + 1)
                    print(f"Decoded substring: {string}")
                    result += num * string
                    i = end
                    num = 0
                elif c == ']':
                    print("Found closing bracket ']'")
                    return result, i
                else:
                    result += c

                i += 1

            return result, i

        # Initiate the recursion and return the decoded result.
        return recurse(s, 0)[0]


# Complexity

# Time complexity: O(n), where n is the length of the input string.
# Each character is processed once in the recursion.

# Space complexity: O(m), where m is the maximum recursion depth.
# The depth of recursion depends on the nesting of brackets in the input string.

```

'''




from typing import List
class Solution:
    def decodeString(self, s: str) -> str:

        # Intuition
        # We can use a recursive approach to process the string and build the decoded result.
        # At each step, we handle digits, opening brackets, closing brackets, and characters.

        # Approach
        # We define a recursive function 'recurse' that takes the input string and the current position as parameters.
        # The function processes the string character by character, handling digits, brackets, and characters accordingly.
        # We use a while loop to iterate through the string and accumulate the decoded result.

        # Pseudo Code
        # def recurse(s, pos):
        #     result = ""
        #     i, num = pos, 0
        #     while i < len(s):
        #         c = s[i]
        #         if c.isdigit():
        #             num = num * 10 + int(c)
        #         elif c == '[':
        #             string, end = recurse(s, i + 1)
        #             result += num * string
        #             i = end
        #             num = 0
        #         elif c == ']':
        #             return result, i
        #         else:
        #             result += c
        #         i += 1
        #     return result, i
        #
        # We initiate the recursion with recurse(s, 0) and return the decoded result.

        def recurse(s, pos):
            result = ""
            i, num = pos, 0

            while i < len(s):
                c = s[i]
                print(f"Processing character: {c}")

                if c.isdigit():
                    num = num * 10 + int(c)
                elif c == '[':
                    print("Found opening bracket '['")
                    string, end = recurse(s, i + 1)
                    print(f"Decoded substring: {string}")
                    result += num * string
                    i = end
                    num = 0
                elif c == ']':
                    print("Found closing bracket ']'")
                    return result, i
                else:
                    result += c

                i += 1

            return result, i

        # Initiate the recursion and return the decoded result.
        return recurse(s, 0)[0]


# Complexity

# Time complexity: O(n), where n is the length of the input string.
# Each character is processed once in the recursion.

# Space complexity: O(m), where m is the maximum recursion depth.
# The depth of recursion depends on the nesting of brackets in the input string.

sol = Solution()
print(sol.decodeString("3[a]2[bc]"))
print(sol.decodeString("3[a2[c]]"))
print(sol.decodeString("2[abc]3[cd]ef"))
