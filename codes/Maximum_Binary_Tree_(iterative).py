class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        root = None
        stack = []
        
        if len(nums)>0:
            stack.append((0,len(nums)-1,None, None))
        
        while len(stack)>0:
            start, end, parent, isLeft = stack.pop()
            
            max_i = start
            max_num = nums[start]

            for i in range(start, end+1):
                if nums[i]>max_num:
                    max_num = nums[i]
                    max_i = i
            
            cur = TreeNode(max_num)
            
            if parent:
                if isLeft:
                    parent.left = cur
                else:
                    parent.right = cur
            else:
                root = cur
            
            if start<max_i:
                stack.append((start, max_i-1, cur, True))
            
            if max_i<end:
                stack.append((max_i+1, end, cur, False))
            
        return root
