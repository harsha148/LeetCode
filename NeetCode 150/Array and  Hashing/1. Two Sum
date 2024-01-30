class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Dict={}
        result=[]
        for i in range(len(nums)):
            if((target-nums[i]) in Dict):
                result.append(Dict[target-nums[i]])
                result.append(i)
                break
            Dict[nums[i]]=i
        return result
        
            
        
