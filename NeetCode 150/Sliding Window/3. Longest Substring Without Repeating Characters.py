class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)==0):
            return 0
        left=0
        right=0
        Dict={}
        maxlen=1
        while(right<len(s)):
            if(s[right] in Dict):
                if(Dict[s[right]]>=left):
                    left=Dict[s[right]]+1
                Dict[s[right]]=right
            else:
                Dict[s[right]]=right
            maxlen=max(maxlen,right-left+1)
            right+=1
        return maxlen
