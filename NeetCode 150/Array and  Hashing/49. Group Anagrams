class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Dict={}
        for i in range(len(strs)):
            if(str(sorted(strs[i])) in Dict):
                Dict[str(sorted(strs[i]))].append(strs[i])
            else:
                Dict[str(sorted(strs[i]))]=[strs[i]]
        results=[]
        for key in Dict.keys():
            results.append(Dict[key])
        return results
        
