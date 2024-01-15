Print binary Tree:

```
defprint_binary_tree(self, node=None, level=0, prefix="Root: ", arrow="   -> "):
        if node isNone:
            node = self    print(" " * (level * 4) + prefix + str(node.value))
        if node.left isnotNoneor node.right isnotNone:
            if node.left isnotNone:
                print(" " * ((level + 1) * 4) + arrow + "Left:")
                self.print_binary_tree(node.left, level + 2, prefix="L: ", arrow="   -> ")
            if node.right isnotNone:
                print(" " * ((level + 1) * 4) + arrow + "Right:")
                self.print_binary_tree(node.right, level + 2, prefix="R: ", arrow="   -> ")
```
