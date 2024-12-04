def maxProfit(prices):
    profit = 0
    for i in range(1, len(prices)):
        # Add the profit for every increase
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit
