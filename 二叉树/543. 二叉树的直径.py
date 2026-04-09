# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # ans=0
        # mini=0
        # def dfs(node,depth):
        #     if node is None:
        #         return
        #     depth+=1
        #     nonlocal ans
        #     nonlocal mini
        #     ans=max(depth,ans)
        #     mini=min(depth,mini)
        #     dfs(node.left,depth)
        #     dfs(node.right,depth)
        # dfs(root,0)   
        # return ans + mini

        ans=0
        def dfs(node):
            if node is None:
                return -1
            l_len=dfs(node.left)+1
            r_len=dfs(node.right)+1
            nonlocal ans
            ans = max(ans,l_len+r_len)
            return max(l_len,r_len)
            #？，为什么是return这个。ans一路递归已经得到我想要的了，为什么要return。
            #对，ans 的确已经在“记录最终答案”了。
            # 但问题是：

            # 父节点更新自己的 ans 时，还需要知道你这棵子树的深度。

            # 所以虽然最终答案存在 ans 里，

            # 递归过程本身仍然必须 return 某个值给父节点用。
        dfs(root)

        return ans
        