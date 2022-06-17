# a tree is an undirected graph that contains no cycles
# given a tree with n nodes (1 to n), with one additional edge added, return the extraneous edge.
# return the edge that can be removed so that the resultant graph is a tree of n nodes.  


#one thing we know is that if we have n nodes and n edges then our input MUST have a cycle
def redundant_connections(edges):
  #initialize each node to be its own parent, initialize all ranks to 1
  parent = [i for i in range(len(edges)+1)] #because 1 to n
  rank = [1] * (len(edges)+1)
  
  def find(n):
    p = parent[n]
    while p != parent[p]:
      parent[p] = parent[parent[p]]
      p = parent[p]
    return p

  #return False if already merged
  def union(n1, n2):
    p1, p2 = find(n1), find(n2)
    if p1 == p2:
      return False #already merged, they have the same parent
      #trying to merge two nodes that already have the same parent is redundant
    if rank[p1] > rank[p2]:
      parent[p2] = p1
      rank[p1] += rank[p2]
    else:
      parent[p1] = p2
      rank[p2] += rank[p1]
    return True

  
  for n1, n2 in edges:
    if not union(n1, n2):
      return [n1, n2]
    

def main():
  print(redundant_connections([[1,2], [1,3], [2,3]])) #any of the three can be removed, but we want [2,3] because it's last
  print(redundant_connections([[1,2],[2,3],[3,4],[1,4],[1,5]])) #should still remove [2,3 ]

main()