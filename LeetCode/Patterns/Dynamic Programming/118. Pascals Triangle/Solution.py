class Solution(object):
    def generate(self, numRows):
        result=[]
        if numRows==0:
            return result

        f_row=[1]
        result.append(f_row)
        
        for i in range(1,numRows):
            p_row=result[i-1]
            c_row=[1]

            for j in range(1,i):
                c_row.append(p_row[j-1]+p_row[j])
            c_row.append(1)
            result.append(c_row)
        return result
        