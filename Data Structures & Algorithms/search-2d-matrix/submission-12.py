class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS - 1
        while top <= bot:
            m = (top + bot) // 2
            if target > matrix[m][-1]:
                top = m + 1
            elif target < matrix[m][0]:
                bot = m - 1
            else:
                break
        if not (top <= bot):
            return False
        
        m = (top + bot) // 2
        left, right = 0, COLS - 1
        while left <= right:
            mid = (left + right) // 2
            if target > matrix[m][mid]:
                left = mid + 1
            elif target < matrix[m][mid]:
                right = mid - 1
            else:
                return True
        return False
        