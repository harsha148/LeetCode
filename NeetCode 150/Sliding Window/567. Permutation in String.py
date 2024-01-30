class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charsInSubstring={}
        for i in range(len(s1)):
            if s1[i] in charsInSubstring:
                charsInSubstring[s1[i]]+=1
            else:
                charsInSubstring[s1[i]]=1
        left=0
        right=len(s1)-1
        charsInSubstring2={}
        if(len(s2)<right):
            return False
        for i in range(right):
            if s2[i] in charsInSubstring2:
                charsInSubstring2[s2[i]]+=1
            else:
                charsInSubstring2[s2[i]]=1
        while(right<len(s2)):
            if( s2[right] in charsInSubstring2):
                charsInSubstring2[s2[right]]+=1
            else:
                charsInSubstring2[s2[right]]=1
            if(charsInSubstring ==charsInSubstring2 ):
                return True
            if(s2[left] in charsInSubstring2):
                charsInSubstring2[s2[left]]-=1
                if(charsInSubstring2[s2[left]]==0):
                    charsInSubstring2.pop(s2[left])
            left+=1
            right+=1
            
        return False
