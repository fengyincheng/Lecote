from collections import deque

class TreeNode:
    def __init__(self,val=0):
        self.val = val
        self.left = None
        self.right = None
    def build_tree(arr):
        if not arr:
            return None
        root = TreeNode(arr[0])
        q = deque([root])
        i = 1

        while q and i < len(arr):
            node = q.popleft()

            if i < len(arr) and arr[i] is not None:
                node.left = TreeNode(arr[i])
                q.append(node.left)
            i += 1

            if i < len(arr) and arr[i] is not None:
                node.right = TreeNode(arr[i])
                q.append(node.right)
            i += 1

        return root