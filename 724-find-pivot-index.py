class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        total = sum(nums)
        last_sum = 0

        for i in range(len(nums)):
            if  last_sum == total - nums[i] - last_sum:
                return i
            
            last_sum += nums[i]

        return -1