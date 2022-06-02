#given a list of houses, return the maximum haul you could get from robbing these houses.
#you are not able to rob adjacent houses without the police being called

from typing import List

#same concept as stairs problem, except our options are to take the max value up to the previous house or the max value of two houses ago + the current house
def house_robber(houses: List[int]) -> int: 
  rob1, rob2 = 0, 0
  #[rob1, rob2, n, n+1, n+2 ...]

  for house in houses:
    rob1, rob2 = rob2, max(house + rob1, rob2)
  
  return rob2 #this will be the max value for all houses once the loop finishes

def main():
  print(house_robber([1,2,3,1]))
main()

#complexity: 
#time: O(n), go through each house and set value
#space: O(1), always two values