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



#good Nodes in Binary Tree
#time complexity: O(n)
#space complexity: O(n)
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, max_value):
            if node is None:
                return 0
            
            count=0
            
            if node.val>=max_value:
                count+=1

            max_value=max(max_value,node.val )
            count+=dfs(node.left,max_value)
            count+=dfs(node.right,max_value)

            return count
        
        return dfs(root,root.val)
    



#Path Sum III
#time complexity: O(n^2)
#space complexity: O(n)

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        

        def findPath(node,target):
            
            if node is None:
                return 0
            
            count=0

            if(node.val==target):
                count+=1

            count+=findPath(node.left,target-node.val)
            count+=findPath(node.right,target-node.val)

            return count

        if root is None:
            return 0
        return (
            findPath(root,targetSum)
            + self.pathSum(root.left,targetSum)
            + self.pathSum(root.right,targetSum)
        )