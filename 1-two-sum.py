class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hashmap = {}

        for i in range(len(nums)):
            item = nums[i]
            
            if (hashmap.get(item) is not None):
                return [hashmap.get(item), i]
            
            sub = target - item
            hashmap[sub] = i