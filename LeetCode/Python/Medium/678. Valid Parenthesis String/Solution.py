class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=h=0
        for i in s:
            l+=((i=='(')<<1)-1
            h+=((i!=')')<<1)-1
            if h<0:
                return False
            l=max(l,0)
        return l==0