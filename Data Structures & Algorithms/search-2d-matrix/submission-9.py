class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        top, bot = 0, rows - 1
        while top <= bot:
            r = (top + bot) // 2
            if target > matrix[r][-1]:
                top = r + 1
            elif target < matrix[r][0]:
                bot = r - 1
            else:
                break
        if not (top <= bot):
            return False
        # r = (top + bot) // 2
        left, right = 0, cols - 1
        while left <= right: 
            m = (left + right) // 2
            if target > matrix[r][m]:
                left = m + 1
            elif target < matrix[r][m]:
                right = m - 1
            else:
                return True
        return False


               
        
        
        
        
        
        #     m = (top - bot) // 2
        #     if target >= matrix[m][0] and target <= matrix[m][cols]:
        #         left = 
        #     elif target < matrix[m][0]:
        #         bot = m - 1
        #     elif target > matrix[m][cols]:
        #         top  = m + 1
        # left, right = 0, cols - 1
        # while left <= right:
        #     m = (right - left) // 2
        #     if target < matrix[m]