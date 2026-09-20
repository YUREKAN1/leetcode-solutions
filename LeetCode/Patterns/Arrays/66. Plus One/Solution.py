class Solution(object):
    def plusOne(self, digits):
        n=len(digits)
        for i in range(n-1,-1,-1):
            if digits[i]==9:
                digits[i]=0
                continue
            else:
                digits[i]+=1
                break
        else:
            digits.insert(0,1)
        return digits

            

