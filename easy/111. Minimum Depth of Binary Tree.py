# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root
# node down to the nearest leaf node.
#
# Note: A leaf is a node with no children.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minDepth(root: TreeNode) -> int:
    if not root:
        return 0

    if not root.left:
        return 1 + minDepth(root.right)
    if not root.right:
        return 1 + minDepth(root.left)

    return 1 + min(minDepth(root.left), minDepth(root.right))
