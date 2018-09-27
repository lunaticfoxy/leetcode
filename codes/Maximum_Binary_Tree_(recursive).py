class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums)==0:
            return None
        
        max_i = 0
        max_num = nums[0]
        
        for i, num in enumerate(nums):
            if num>max_num:
                max_num = num
                max_i = i
        
        root = TreeNode(max_num)
        root.left = self.constructMaximumBinaryTree(nums[:max_i])
        root.right = self.constructMaximumBinaryTree(nums[max_i+1:])
        
        return root
        
