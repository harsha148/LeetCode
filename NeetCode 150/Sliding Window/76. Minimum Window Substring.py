class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if(len(t)>len(s)):
            return ''
        minlength=len(s)+1
        freqt={}
        freqs={}
        tfreqs={}
        for i in range(len(t)):
            if t[i] not in freqt:
                freqt[t[i]]=1
            else:
                freqt[t[i]]+=1
        freqtcopy=freqt.copy()
        minleft=-1
        minright=-1
        for i in range(len(t)):
            if s[i] in freqs:
                freqs[s[i]]+=1
            else:
                freqs[s[i]]=1
            if s[i] in freqt:
                if s[i] in tfreqs:
                    if(tfreqs[s[i]]!=freqt[s[i]]):
                        tfreqs[s[i]]+=1
                else:
                    tfreqs[s[i]]=1
        l=0
        r=len(t)-1
        while r<len(s):
            if(tfreqs==freqt):
                if(r-l+1<minlength):
                    minlength=r-l+1
                    minleft=l
                    minright=r
                if s[l] in tfreqs:
                    if(tfreqs[s[l]]==freqs[s[l]]):
                        tfreqs[s[l]]-=1
                        if(tfreqs[s[l]]==0):
                            tfreqs.pop(s[l])
                freqs[s[l]]-=1
                if(freqs[s[l]]==0):
                    freqs.pop(s[l])
                l+=1
            else:
                r+=1
                if(r==len(s)):
                    break
                if s[r] in freqs:
                    freqs[s[r]]+=1
                else:
                    freqs[s[r]]=1
                if(s[r] in freqt):
                    if(s[r] in tfreqs):
                        if(tfreqs[s[r]]!=freqt[s[r]]):
                            tfreqs[s[r]]+=1
                    else:
                        tfreqs[s[r]]=1
        if minleft==-1 and minright==-1:
            return ''
        return s[minleft:minright+1]
                
