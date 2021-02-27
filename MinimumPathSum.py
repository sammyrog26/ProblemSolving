# 1,3,5
# 2,1,1 ------> Sum= 8
# 2,4,3


def min_path_sum(grid):
    rows = len(grid)
    cols = len(grid[0])
    print(rows, cols)
    dp = [[0]*rows]*cols
    
    dp[0][0] = grid[0][0]

    for col in range(1, cols):        
        dp[0][col] = dp[0][col-1] + grid[0][col]
        # print(dp)

    for row in range(1, rows):
        dp[row][0] = dp[row-1][0] + grid[row][0]
        print(dp)

    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])    

    print(dp[rows-1][cols-1])


if __name__ == "__main__":
    l = [[1,1,2],[2,3,1],[4,1,2]]
    min_path_sum(l)