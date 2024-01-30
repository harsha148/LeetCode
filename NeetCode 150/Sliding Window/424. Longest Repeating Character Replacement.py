class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        right=0
        freq={}
        maxfreq=0
        maxlen=0
        while(right<len(s)):
            if(s[right] in freq):
                freq[s[right]]+=1
            else:
                freq[s[right]]=1
            maxfreq=max(maxfreq,freq[s[right]])
            if(right-left+1-maxfreq>k):
                freq[s[left]]-=1
                left+=1
            else:
                # print()
                maxlen=max(maxlen,right-left+1)
            right+=1
        return maxlen
