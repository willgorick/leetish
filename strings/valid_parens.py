from collections import deque

def isValid(s: str) -> bool:
        stack = deque()
        for c in s:
            if c == "(":
                stack.append("(")
            elif c == "{":
                stack.append("{")
            elif c == "[":
                stack.append("[")
            elif c == ")":
                if not len(stack) or stack.pop() != "(":
                    return False
            elif c == "}":
                if not len(stack) or stack.pop() != "{":
                    return False
            elif c == "]":
                if not len(stack) or stack.pop() != "[":
                    return False
        return True if len(stack) == 0 else False

def main():
  print(isValid("()[]{}"))

main()