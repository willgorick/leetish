#you can climb stairs in increments of two steps or one step
#how many ways can you climb to get to step n

def climbStairs(n: int) -> int:
  one, two = 1, 1
  for i in range(n-1):
    one, two = one + two, one
  return one

def main():
  print(climbStairs(8))

main()