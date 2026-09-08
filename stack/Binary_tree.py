# maxDepth of Binary Tree
#time complexity: O(n)
#space complexity: O(n)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))


#leaf Similar Trees
#time complexity: O(n)
#space complexity: O(n)
class Solution:
    def leafSimilar(self, root1, root2):

        leaves1 = []
        leaves2 = []

        def dfs(root, leaves):
            if root is None:
                return

            if root.left is None and root.right is None:
                leaves.append(root.val)
                return

            dfs(root.left, leaves)
            dfs(root.right, leaves)

        dfs(root1, leaves1)
        dfs(root2, leaves2)

        return leaves1 == leaves2