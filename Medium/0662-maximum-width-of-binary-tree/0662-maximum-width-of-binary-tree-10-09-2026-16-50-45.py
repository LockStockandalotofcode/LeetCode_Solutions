from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        if not root: 
            return 0

        queue = deque([(root, 1)])
        level_width = 1
        max_width = 0
        while queue:
            size = len(queue)
            leftmost_node_index = queue[0][1]
            rightmost_node_index = queue[-1][1]
            level_width = rightmost_node_index - leftmost_node_index + 1
            max_width = max(max_width, level_width)
            for i in range(size):
                curr, index = queue.popleft()
                # process current node
                if curr.left:
                    queue.append((curr.left, 2*index))
                if curr.right:
                    queue.append((curr.right, (2*index + 1)))

        return max_width