from typing import List

#what's the fewest number of coins (from the denominations provided) you can use to get to the specified amount
def coinChange(coins: List[int], amount: int) -> int:
  dp = [amount+1] * (amount + 1)
  dp[0] = 0
  for a in range(1, amount+1):
    for c in coins:
      if a - c >= 0:
        dp[a] = min(dp[a], 1 + dp[a-c]) #either you stick with the current minimum number of coins for that value, or you take the minimum number minus the current count + 1 (adding the current coin)
  return dp[amount] if dp[amount] != amount+1 else -1

def main():
  print(coinChange([1,3,4,5], 7))
  print(coinChange([1,3,4,5], 9))
  print(coinChange([1,3,4,5], 11))
  print(coinChange([3,4,5], 2))
  print(coinChange([3,5], 6))
main()

# complexity:
# time: O(n * m) where n is our target amount and m is the number of different coin values
# space: O(n), we initialize an array of size n + 1