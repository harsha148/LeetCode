class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        len1=len(nums)-1
        for i in range(len1):
            if(nums[i]==nums[i+1]):
                return True
        return False
