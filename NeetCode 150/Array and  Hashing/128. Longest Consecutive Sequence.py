class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if(len(nums)==0):
            return 0
        maxlen=1
        l=1
        # for(i in range(len(nums)-1))
        for i in range(len(nums)-1):
            if(nums[i]==nums[i+1]):
                continue
            if(nums[i]+1==nums[i+1]):
                l+=1
            else:
                l=1
            if(l>maxlen):
                maxlen=l
        return maxlen
        
