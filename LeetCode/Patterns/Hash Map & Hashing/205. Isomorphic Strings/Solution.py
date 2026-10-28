class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        chs={}
        cht={}
        for i in range(len(s)):
            if s[i] not in chs:
                chs[s[i]]=i
            if t[i] not in cht:
                cht[t[i]]=i
            if chs[s[i]]!=cht[t[i]]:
                return False
        return True