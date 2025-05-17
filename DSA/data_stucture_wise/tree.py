import collections
from typing import Optional

# Step 1: TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Step 2: Function to build binary tree from level-order input
def build_tree(level_order):
    if not level_order or level_order[0] is None:
        return None

    root = TreeNode(level_order[0])
    queue = collections.deque([root])
    i = 1

    while queue and i < len(level_order):
        current = queue.popleft()

        if level_order[i] is not None:
            current.left = TreeNode(level_order[i])
            queue.append(current.left)
        i += 1

        if i < len(level_order) and level_order[i] is not None:
            current.right = TreeNode(level_order[i])
            queue.append(current.right)
        i += 1

    return root

# Step 3: Top View function
def topView(root: TreeNode):
    INF = 10 ** 10
    tops = {}
    leftMost = INF
    rightMost = -INF

    q = collections.deque([(0, root)])
    while q:
        for i in range(len(q)):
            idx, node = q.popleft()
            leftMost = min(leftMost, idx)
            rightMost = max(rightMost, idx)

            if idx not in tops:
                tops[idx] = node.val
            
            if node.left:
                q.append((idx-1, node.left))
            if node.right:
                q.append((idx+1, node.right))
    ans = []
    for i in range(leftMost, rightMost+1):
        ans.append(tops[i])

    return ans
# Step 4: Example usage
level_order_input = [1, 2, 3, None, 4, 5, None]
root = build_tree(level_order_input)
print(topView(root))  # Output could be [2, 1, 3, 5]
