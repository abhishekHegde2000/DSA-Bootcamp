Print binary Tree:

Certainly! Here's the modified `display_preorder` method using f-strings:

```python
class Solution:
    def display_preorder(self, root, level=0):
        if root is not None:
            print(f'Level {level}: {" " * 4 * level}-> {root.val}')
            self.display_preorder(root.left, level + 1)
            self.display_preorder(root.right, level + 1)
```

Now, the output will still include the level information in the print statement, but using f-strings for a more concise format:

```python
# Display the binary tree using the updated display_preorder method
solution.display_preorder(root)
```

Output:

```
Level 0: -> 1
Level 1:     -> 2
Level 2:         -> 4
Level 2:         -> 5
Level 1:     -> 3
```

Feel free to use this modified version based on your preferences.
