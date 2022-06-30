def maxDepth(s: str) -> int:
        max_d = 0
        stack = deque()
        for i in range(len(s)):
            if s[i] == "(":
                stack.appendleft(True)
                max_d = max(max_d, len(stack))
            elif s[i] == ")":
                stack.popleft()
        if len(stack):
            return -1 #invalid
        return max_d

def main():
  print(maxDepth("(1+(2*3)+((8)/4))+1"))

main()