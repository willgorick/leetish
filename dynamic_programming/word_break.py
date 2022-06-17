#O(n * m), where n is the length of the string s and m is the number of words

def word_break(s, wordDict):
  n = len(s)
  dp = [False for _ in range(n+1)]
  dp[n] = True #position past the string is true
  for i in range(n-1, -1, -1): #O(n)
    for word in wordDict: #O(m)
      if (i + len(word)) <= n and s[i: i+len(word)] == word:
        dp[i] = dp[i + len(word)] #dp[i] is equal to the value for the index + the length of our word (i.e., when we get to index 4, and see that "code" fits, we grab True from 8, and then at 0 when we see that "leet" fits we grab True from 4)
      if dp[i]:
        break
  return dp[0]

    


def main():
  print(word_break("neetcode", ["leet", "neet", "code"]))

main()