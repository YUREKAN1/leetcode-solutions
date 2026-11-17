class Solution:
    def firstUniqChar(self, s: str) -> int:
        f={}
        for c in s:
            f[c]=1+f.get(c,0)
        for i,c in enumerate(s):
            if f[c]==1:
                return i
        return -1