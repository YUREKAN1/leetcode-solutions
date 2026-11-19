class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i,j,carry=len(num1)-1,len(num2)-1,0
        result=""
        while i>=0 or j>=0 or carry:
            d1=int(num1[i]) if i>=0 else 0
            d2=int(num2[j]) if j>=0 else 0
            t=d1+d2+carry
            carry=t//10
            result=str(t%10)+result
            i-=1
            j-=1
        return result