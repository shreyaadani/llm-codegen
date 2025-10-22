def min_cost_path(cost, m, n):
    R = len(cost)
    C = len(cost[0])
    dp = [[0 for _ in range(C)] for _ in range(R)]
    dp[0][0] = cost[0][0]
    for i in range(1, R):
        dp[i][0] = dp[i-1][0] + cost[i][0]
    for j in range(1, C):
        dp[0][j] = dp[0][j-1] + cost[0][j]
    for i in range(1, R):
        for j in range(1, C):
            dp[i][j] = cost[i][j] + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]