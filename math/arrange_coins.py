def arrangeCoins(n: int) -> int:
        #summation from 1 to n = (n/2) * (n+1)
        l, r = 1, n
        res = 0
        
        while l <= r:
            mid = (l + r) // 2
            toComplete = (mid/2) * (mid+1)
            if toComplete > n:
                r = mid - 1
            else:
                res = max(mid, res)
                l = mid + 1
                
        return res

def main():
  print(arrangeCoins(5))

main()