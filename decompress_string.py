# Your input is a compressed string of the format number[string] and the decompressed output form should be the string written number times
from collections import deque

def decompress_string(string: str):
  return decompress_recursive(string, 0)

def decompress_recursive(string: str, repeat_count: int):
  print(string)
  bracket_queue = deque()
  curr_count_string = ''
  repeat_string = ''
  solution = ''
  for char in string:
    if char.isalpha():
      if len(bracket_queue):
        repeat_string += char
      else:
        solution += char
    elif char.isnumeric():
      curr_count_string += char
    elif char == '[':
      bracket_queue.append('[')
    elif char == ']':
      bracket_queue.popleft()
      if len(bracket_queue) == 0:
        solution += decompress_recursive(repeat_string, int(curr_count_string))
        repeat_string = ''
        curr_count_string = ''

  if repeat_count:
    solution *= repeat_count
  return solution



def main():
  # print(decompress_string('3[abc]'))
  # print(decompress_string('3[abc]4[ab]c'))
  # print('xy'*3)
  print(decompress_string('2[3[a]b]'))
main()