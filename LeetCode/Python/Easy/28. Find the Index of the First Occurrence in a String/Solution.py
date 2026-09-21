class Solution(object):
    def strStr(self, haystack, needle):
        r=-1
        if needle in haystack:
            r=haystack.index(needle[0])
        return r
        