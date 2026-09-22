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





  #Longest ZigZag Path in a Binary Tree
#time complexity: O(n)
#space complexity: O(n)

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
 
        ans = 0

        def dfs(node, direction, length):
            nonlocal ans

            if node is None:
                return

            ans = max(ans, length)

            if direction == "left":
                dfs(node.left, "right", length + 1)
                dfs(node.right, "left", 1)

            else:
                dfs(node.right, "left", length + 1)
                dfs(node.left, "right", 1)

        dfs(root, "left", 0)
        dfs(root, "right", 0)

        return ans




    #Lowest Common Ancestor of a Binary Tree
    #time complexity: O(n)
    #space complexity: O(n)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root is None:
            return None

        if root==p or root==q:
            return root

        left=self.lowestCommonAncestor(root.left, p, q)
        right=self.lowestCommonAncestor(root.right, p, q)

        if left is not None and right is not None:
            return root
        
        if left is not None:
            return left
        
        return right        




#Right Side View of Binary Tree
#time complexity: O(n)
#space complexity: O(n)

    class Solution:
    def rightSideView(self, root):

        result = []

        def dfs(node, depth):

            if node is None:
                return

            if depth == len(result):
                result.append(node.val)

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)

        return result



        #Maximum Level Sum of a Binary Tree
        #time complexity: O(n)
        #space complexity: O(n)
from collections import deque

class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:

        queue = deque([root])

        level = 1
        max_sum = float("-inf")
        #answer = 1

        while queue:

            level_sum = 0

            for _ in range(len(queue)):
                node = queue.popleft()

                level_sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                answer = level

            level += 1

        return answer



    #Search in a Binary Search Tree
    #time complexity: O(n)
    #space complexity: O(n)

    class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        

        if root is None:
            return None

        if root.val==val:
            return root

        if val < root.val:
            return self.searchBST(root.left,val)

        return self.searchBST(root.right,val)