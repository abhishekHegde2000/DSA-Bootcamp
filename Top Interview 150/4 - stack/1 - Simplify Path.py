'''
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
Return the simplified canonical path.

 

Example 1:

Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
Example 2:

Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
Example 3:

Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

'''


class Solution:
    def simplifyPath(self, path: str) -> str:
        simplified_path_components = []  # Initialize stack for simplified path
        current_component = ""

        for character in path + "/":
            print(f"Processing character: {character}")

            if character == "/":
                if current_component == "..":
                    if simplified_path_components:
                        print("Moving up one level: Popping from stack")
                        simplified_path_components.pop()
                elif current_component and current_component != ".":
                    print(f"Adding component: {current_component}")
                    simplified_path_components.append(current_component)
                current_component = ""
            else:
                current_component += character

        return "/" + "/".join(simplified_path_components)


sol = Solution()
print(sol.simplifyPath("/home/"))
print(sol.simplifyPath("/..//home/"))
print(sol.simplifyPath("/home//foo/../"))

'''


**# Intuition**

- **Use a stack to manage path components:** Push directories onto the stack, handling ".." by popping and ignoring ".".
- **Build simplified path from stack:** Reconstruct the path from the remaining directories in the stack.

**# Approach**

1. **Initialize an empty stack to store path components.**
2. **Iterate through each character in the input path, including an extra "/" at the end:**
   - **If the character is "/":**
     - If the current component is "..":
       - Pop the top directory from the stack if it's not empty (move up one level).
     - Otherwise, if the current component is not empty and not ".":
       - Push the current component onto the stack.
     - Reset the current component to an empty string.
   - **Else, append the character to the current component.**
3. **Join the remaining components in the stack, separated by "/", and return the simplified path.**

**# Pseudo Code**

```
1. Initialize stack = []
2. For each character in input path + "/":
    a. If character is "/":
        - If current component is "..":
            - Pop top directory from stack if not empty
        - Else if current component is not empty and not ".":
            - Push current component onto stack
        - Reset current component to empty string
    b. Else:
        - Append character to current component
3. Return "/" + "/".join(stack)
```

**# Complexity**

- **Time complexity:** O(n), where n is the length of the input path. Each character is processed at most twice (once in the main loop and potentially once in the stack operations).
- **Space complexity:** O(n), due to the stack potentially holding all path components in the worst case.

**# Code with Debugging Print Statements and Comments**

```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        simplified_path_components = []  # Initialize stack for simplified path
        current_component = ""

        for character in path + "/":
            print(f"Processing character: {character}")

            if character == "/":
                if current_component == "..":
                    if simplified_path_components:
                        print("Moving up one level: Popping from stack")
                        simplified_path_components.pop()
                elif current_component and current_component != ".":
                    print(f"Adding component: {current_component}")
                    simplified_path_components.append(current_component)
                current_component = ""
            else:
                current_component += character

        return "/" + "/".join(simplified_path_components)
```

'''
