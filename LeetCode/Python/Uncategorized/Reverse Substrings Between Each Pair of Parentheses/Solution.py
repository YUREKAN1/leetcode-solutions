class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """

        while "(" in s:
            start=s.rfind("(")
            end=s.find(")",start)
            rev=s[start+1:end][::-1]
            s=s[:start]+rev+s[end+1:]
        return s
        