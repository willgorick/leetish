# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# Return true if you can finish all courses. Otherwise, return false.

from collections import deque
from typing import List

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
  graph = {i: [] for i in range(numCourses)}
  in_degree = {i: 0 for i in range(numCourses)}
  queue = deque()
  sorted_order = []
        
  for pair in prerequisites: #O(v)
    child, parent = pair[0], pair[1]
    in_degree[child] += 1
    graph[parent].append(child)
        
        
  for key in in_degree: #O(E)
    if in_degree[key] == 0:
      queue.append(key)
                
  while queue: #if you encounter nodes that never get to 0 in degree that means they can't be taken
        #O(e)
    vertex = queue.popleft()
    sorted_order.append(vertex)
    for child in graph[vertex]:
      in_degree[child] -= 1
      if in_degree[child] == 0:
        queue.append(child)
  return len(sorted_order) == numCourses

def main():
  print(canFinish(2, [[1,0], [0,1]]))
  print(canFinish(3, [[1,0], [1,2]]))

main()