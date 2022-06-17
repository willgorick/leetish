
# Definition for a Node.
class Node:
  def __init__(self, val = 0, neighbors = None):
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []

from collections import deque 


#breadth first search, for each node, create corresponding nodes for its neighbors, then push those neighbors on to the stack, use a visited set to ensure we don't cycle
def cloneGraph(node: 'Node') -> 'Node':
  if not node:
    return node
  node_to_copy, visited, queue = {}, set(), deque([node])
  while queue:
    curr_node = queue.popleft()
    if curr_node.val in visited:
      continue
    visited.add(curr_node.val)
    if curr_node not in node_to_copy:
      node_to_copy[curr_node] = Node(curr_node.val)
    for neighbor in curr_node.neighbors:
      if neighbor not in node_to_copy:
        node_to_copy[neighbor] = Node(neighbor.val)
      node_to_copy[curr_node].neighbors.append(node_to_copy[neighbor])
      queue.append(neighbor)
            
  return node_to_copy[node]

def main():
  head = Node(1)
  head.neighbors = [Node(2), Node(3), Node(4, [Node(5), Node(6)])]
  new_graph = cloneGraph(head)
  print_queue = deque()
  print_queue.append(new_graph)
  while print_queue:
    node = print_queue.popleft()
    print(node.val)
    for neighbor in node.neighbors:
      print_queue.append(neighbor)
    
main()
        
            