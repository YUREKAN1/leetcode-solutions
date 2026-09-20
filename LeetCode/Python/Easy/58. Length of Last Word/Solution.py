class Solution(object):
    def lengthOfLastWord(self, s):
        count=0
        i=len(s)-1
        while s[i]==' ':
            i-=1
        while i>=0 and s[i].isalpha():
            count+=1
            i-=1
        return count