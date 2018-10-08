class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = 0
        for num in nums:            # 일단 중복 제거
            res ^= num
        
        last_bit = res&-res         # 맨 마지막에 1로 세팅된 비트 체크
        
        val1 = 0
        val2 = 0
        for num in nums:            # 해당 비트가 1인 값들과 0인 값들을 나눠서 xor 하면 중복 제거됨
            if (num&last_bit)==0:
                val1 ^= num
            else:
                val2 ^= num
        
        return [val1, val2]
