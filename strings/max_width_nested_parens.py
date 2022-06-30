from collections import deque

def max_width(parens: str):
  max_wid = 0
  stack = deque()
  start_ind = 0
  for i in range(len(parens)):
    if parens[i] == "(":
      stack.append(True)
    elif parens[i] == ")":
      if len(stack):
        stack.pop()
        if len(stack) == 0:
          max_wid = max(max_wid, i-start_ind+1)
          start_ind = i+1 #start the next paren at the next char, if it's a close we'll just return -1
      else:
        return -1
  return max_wid

def main():
  print(max_width("(())()()((()))")) # six for this ending section ((()))

main()
