def knapsack_recursive(W, wt, val, n):
    # Base Case: No capacity left or no items left
    if n == 0 or W == 0:
        return 0

    # If weight of the current item is more than Knapsack capacity,
    # then this item cannot be included in the optimal solution
    if wt[n-1] > W:
        return knapsack_recursive(W, wt, val, n-1)

    # Return the maximum of two cases:
    # 1. Current item included (Take)
    # 2. Current item not included (Leave)
    else:
        take_item = val[n-1] + knapsack_recursive(W - wt[n-1], wt, val, n-1)
        leave_item = knapsack_recursive(W, wt, val, n-1)
        return max(take_item, leave_item)

# --- How to invoke ---
# n = len(val)
# print(knapsack_recursive(W, wt, val, n))

#########################################################################################

def knapsack_2d(W, wt, val, N):
    # Initialize a 2D DP table with zeros
    # Rows: items (0 to N), Columns: capacity (0 to W)
    dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]

    # Build the table bottom-up
    for i in range(1, N + 1):
        for w in range(1, W + 1):
            if wt[i-1] <= w:
                # Max of (Take current item + value of remaining capacity, Leave current item)
                dp[i][w] = max(val[i-1] + dp[i-1][w - wt[i-1]], dp[i-1][w])
            else:
                # Cannot fit, inherit value from previous item row
                dp[i][w] = dp[i-1][w]

    return dp[N][W]

#########################################################################################

def knapsack_1d(W, wt, val, N):
    # Initialize a 1D DP array with zeros for capacity 0 to W
    dp = [0] * (W + 1)

    for i in range(N):
        # Traverse the capacity backwards to prevent reusing the same item
        for w in range(W, wt[i] - 1, -1):
            # Update the max value for capacity 'w'
            dp[w] = max(dp[w], val[i] + dp[w - wt[i]])

    return dp[W]
