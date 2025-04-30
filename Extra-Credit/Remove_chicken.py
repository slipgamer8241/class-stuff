class BinaryTreeNode:
    def __init__(self, number):
        self.number = number
        self.left = None
        self.right = None

def remove_little_children(root):
    if not root:
        return None

    # Recursively process left and right subtrees
    root.left = remove_little_children(root.left)
    root.right = remove_little_children(root.right)

    # Remove nodes smaller than the root's value
    if root.left and root.left.number < root.number:
        # Replace the left child with its larger subtree (if any)
        if root.left.left and root.left.right:
            # If both subtrees exist, choose the larger one
            root.left = root.left.left if root.left.left.number >= root.left.right.number else root.left.right
        elif root.left.left:
            root.left = root.left.left
        elif root.left.right:
            root.left = root.left.right
        else:
            root.left = None  # Remove the node if it has no children

    if root.right and root.right.number < root.number:
        # Replace the right child with its larger subtree (if any)
        if root.right.left and root.right.right:
            # If both subtrees exist, choose the larger one
            root.right = root.right.left if root.right.left.number >= root.right.right.number else root.right.right
        elif root.right.left:
            root.right = root.right.left
        elif root.right.right:
            root.right = root.right.right
        else:
            root.right = None  # Remove the node if it has no children

    return root