# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = deque()
        
        if not root==None:
            queue.append((root, 0))
        
        res = []
        while len(queue)>0:
            cur, level = queue.popleft()
            
            while len(res)<=level:
                res.append(None)
                
            if res[level]==None or res[level]<cur.val:
                res[level] = cur.val
            
            if cur.left:
                queue.append((cur.left, level+1))
            
            if cur.right:
                queue.append((cur.right, level+1))
        
        return res
