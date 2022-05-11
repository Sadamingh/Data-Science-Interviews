import math

def maxProfit(prices):
    maxProfit, minVal = 0, math.inf
    for price in prices:
        minVal, maxProfit = min(minVal, price), max(maxProfit, price-minVal)
    return maxProfit

print(maxProfit([7,1,5,3,6,4]))
