class Solution:
    def longestPalindrome(self, s: str) -> int:
        c_set=set()
        length=0
        for i in s:
            if i in c_set:
                c_set.remove(i)
                length+=2
            else:
                c_set.add(i)
        if c_set:
            length+=1
        return length