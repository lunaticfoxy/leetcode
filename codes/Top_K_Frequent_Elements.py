from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cnt = dict(Counter(nums))
        cnt = list(zip(*sorted(cnt.items(), key=lambda kv: kv[1], reverse=True)))[0]
        
        return cnt[:k]
