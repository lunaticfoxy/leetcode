class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = 0
        second = 0
        third = 0
        for num in nums:
            third = second & num                            # 3번 나온 값은 2번나온값&현재값
            second = (second | (first & num)) & (~third)    # 2번 나온 값은 한번나온값&현재값 + 원래2번나온값 - 3번나온값
            first = (first | num) & (~second) & (~third)    # 1번 나온 값은 현재값 - 2번나온값 - 3번나온값
        return first
