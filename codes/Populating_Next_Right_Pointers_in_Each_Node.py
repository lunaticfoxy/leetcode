# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
from collections import deque

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        queue = deque()
        
        if root:
            queue.append([root, 0])
        
        before = None
        before_level = -1
        
        while len(queue)>0:
            cur, cur_level = queue.popleft()
            
            if before_level==cur_level and before:
                before.next = cur
            
            before = cur
            before_level = cur_level
            
            if cur.left:
                queue.append([cur.left, cur_level+1])
            
            if cur.right:
                queue.append([cur.right, cur_level+1])
            
        
