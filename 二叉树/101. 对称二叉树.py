# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(a,b):
            if a is None and b is None:
                return True
            if a is None and b is not None:
                return False
            if a is not None and b is  None:
                return False
            if a.val != b.val:
                return False
       
            return dfs(a.right,b.left) and dfs(a.left,b.right)
            #为什么要这样？指dfs(a.right,b.left) and (a.left,b.right)
            """
            因为题目要判断：

            两棵子树是否互为镜像

            镜像的定义是：

            左树的左  ↔ 右树的右
            左树的右  ↔ 右树的左
                  a                b
                /   \            /   \
            a.left a.right   b.left b.right

           ** 那我不能 a.left a.right   b.left b.right吗？**
           不能，因为那样比较的是：

            两棵树长得是否一样

            而不是：

            两棵树是否互为镜像
            
            """
                
        return dfs(root.left,root.right)  


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def Tree(self,p:Optional[TreeNode],q: Optional[TreeNode])->bool :
        if p is None or q is None:
            return p is q
        return p.val==q.val and self.Tree(p.left,q.right) and self.Tree(p.right,q.left)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.Tree(root.left,root.right) 