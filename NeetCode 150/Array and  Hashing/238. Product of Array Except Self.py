class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        backProduct=1
        frontProduct=1
        results=[1 for i in range(len(nums))]
        for i in range(len(nums)):
            if(i==0):
                continue
            backProduct=backProduct*nums[i-1]
            results[i]*=backProduct
        for i in range(len(nums)):
            if(i==0):
                continue
            frontProduct*=nums[len(nums)-i]
            results[len(nums)-i-1]*=frontProduct
        return results
