# 102. 二叉树的层序遍历

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ans=[]
        q=deque([root])
        """
              3
            / \
            9  20
            /  \
            15   7
        q = [3]
        ans = []
        弹出 3
        vals=[3]
        加入 9,20
        ans=[[3]]
        q=[9,20]        
        
        """
        while q:
            vals=[]
            for _ in range(len(q)):
                node = q.popleft()
                vals.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            ans.append(vals)
        return ans
        #思路参考灵神
        # https://www.bilibili.com/video/BV1hG4y1277i/
        