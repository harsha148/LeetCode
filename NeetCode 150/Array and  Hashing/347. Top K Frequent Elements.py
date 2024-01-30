class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result=[]
        freq=1
        dict={}
        for j in range(len(nums)):
            if(nums[j] in dict):
                dict[nums[j]]+=1
            else:
                dict[nums[j]]=1
        dict1=sorted(dict.items(),key=lambda item: item[1],reverse=True)
        results=[]
        i=0
        for i in range(len(dict1)):
            if(i==k):
                break
            results.append(dict1[i][0])
        return results
            
            
                
        
