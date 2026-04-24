### Union-Find Algorithm Approach ###

"""
Use Disjoint Set Union (Union-Find) to track connected components while adding edges one by one.

* Initially, every node is its own component. 
* When we add an edge (u, v):
    * If u and v are already in the same component, adding this edge creates a cycle.
    * That edge is exactly the redundant connection.
If they are in different components, we safely merge them.

Because edges are processed in order, the first edge that fails to union is the answer.

"""

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 1. Initialize Disjoint Union Set, where each node is its own parent 
        
        # Create parent array, initially each node is its own parent 
        # +1 because nodes are labeled from 1 to n
        # parent of index i is i
        parent = [i for i in range(len(edges) + 1)]

        # Create Rank (size) array, initially every node by itself so all ranks = 1
        rank = [1] * (len(edges) + 1)

        # Function to find the root (leader) of node n
        def find(n):
            # Start from node n, get its parent
            p = parent[n]
            
            # Keep going up until we reach the root
            # Root = node that points to itself
            while p != parent[p]:
                # Perform path compression 
                parent[p] = parent[parent[p]]
                p = parent[p]
            # Return the root of node n
            return p

        # Function to connect two nodes
        def union(n1, n2):
            # Find roots of both nodes
            p1, p2 = find(n1), find(n2)
            
            # If both nodes have the same root → already connected
            # Adding this edge creates a cycle
            # So return False
            if p1 == p2:
                return False
            
            # Compare sizes of the two trees
            # Attach smaller tree under bigger tree 
            # Update size of the new merged tree
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            # Union successful (no cycle formed)
            return True

        # Go through every edge in the graph
        for n1, n2 in edges:
            # Try to connect nodes
            # If union returns False → cycle detected
            if not union(n1, n2):
                # Return the edge that caused the cycle
                return [n1, n2]







        