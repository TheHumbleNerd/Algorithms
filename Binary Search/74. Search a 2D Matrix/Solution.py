class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l, r = 0, (rows*cols)-1

        while l <= r:
            m = l + ((r-l)//2)
            rIndex = m // cols
            cIndex = m - (rIndex*cols)
            if matrix[rIndex][cIndex] < target:
                l = m + 1
            elif matrix[rIndex][cIndex] > target:
                r = m - 1
            else:
                return True
        return False
