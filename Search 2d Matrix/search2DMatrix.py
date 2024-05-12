class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Rows,Cols = len(matrix),len(matrix[0])
        #get dimension 
        top,bot = 0,Rows-1
        while top<=bot:
            row = (top+bot)//2
            if target>matrix[row][-1]:
                top = row+1
            elif target < matrix[row][0]:
                bot = row-1
            else:
                break
            #2nd phase of binary search
        if not (top<=bot):
            return False
        row = (top+bot)//2
        lf,r = 0,Cols-1
        while lf<=r:
            m = (lf+r)//2
            if target>matrix[row][m]:
                lf = m+1
            elif target<matrix[row][m]:
                r = m-1
            else:
                return True
        return False