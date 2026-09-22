class Solution(object):
    def reverseVowels(self, s):
        left=0
        right=len(s)-1
        v=['a','e','i','o','u','A','E','I','O','U']
        l=[]
        f=""
        for i in s:
            l.append(i)

        while left<right:
            while left<right and l[left] not in v:
                left+=1
            while left<right and l[right] not in v:
                right-=1
            l[left],l[right]=l[right],l[left]
            left+=1
            right-=1
        return ''.join(l)
        

        