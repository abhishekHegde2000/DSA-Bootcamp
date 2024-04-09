class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def is_balanced(root):
    if root is None:
        return True
    left_height = get_height(root.left)
    right_height = get_height(root.right)
    if abs(left_height - right_height) <= 1 and is_balanced(root.left) and is_balanced(root.right):
        return True
    return False


def get_height(root):
    if root is None:
        return 0
    return 1 + max(get_height(root.left), get_height(root.right))


# Example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

if is_balanced(root):
    print("The tree is balanced")
else:
    print("The tree is not balanced")
