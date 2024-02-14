class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.preSum = [[0]*(len(matrix[0]) + 1) for i in range(len(matrix) + 1)]
        self.row = len(matrix) + 1
        self.col = len(matrix[0]) + 1

        for i in range(1, self.row):
            for j in range(1 , self.col):
                self.preSum[i][j] = self.preSum[i][j - 1 ] + self.preSum[i -1][j] + matrix[i - 1][j - 1] - self.preSum[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.preSum[row2 + 1][col2 + 1] - self.preSum[row1][col2 + 1] - self.preSum[row2 + 1][col1] + self.preSum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)