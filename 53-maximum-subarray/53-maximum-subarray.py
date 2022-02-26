class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        greater_sum = nums[0]
        sum_ = 0
        for i in range(len(nums)):
            sum_ = sum_ + nums[i]
            if sum_>greater_sum:
                greater_sum = sum_
            if sum_ < 0:
                sum_ = 0

        return greater_sum
    
                