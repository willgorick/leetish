#basically, implement selection sort (which is optimal) and keep track of how many swaps were needed
def minSwaps(arr):
  n = len(arr)
  ans = 0
  sorted_arr = arr.copy()

  # Dictionary which stores the
  # indexes of the input array
  h = {}
 
  sorted_arr.sort()

  for i in range(n):
       
      h[arr[i]] = i #map of value to index
     
  for i in range(n):
 
    # This is checking whether
    # the current element is
    # at the right place or not
    if (arr[i] != sorted_arr[i]):
        ans += 1
        init = arr[i]

        # If not, swap this element
        # with the index of the
        # element which should come here
        # h[sorted_arr[i]] is the index of the element that should be at our current index (the index of the number that belongs here)
        arr[i], arr[h[sorted_arr[i]]] = arr[h[sorted_arr[i]]], arr[i]

        # Update the indexes in
        # the hashmap accordingly
        # set our now swapped out value's corresponding value in the map (it's index) to the value we value we swapped with's index 
        h[init] = h[sorted_arr[i]]
        h[sorted_arr[i]] = i #set that swapped value's index to our original i index
             
  return ans

def main():
  arr = [1, 5, 4, 3, 2]
  print(minSwaps(arr))

  arr = [6, 0, 3, 5, 2, 4, 1]
  print(minSwaps(arr))

main()