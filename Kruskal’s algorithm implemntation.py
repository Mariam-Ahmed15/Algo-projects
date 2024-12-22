class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))  # Initially, each node is its own parent
        self.rank = [0] * n  # Initially, all trees have rank 0
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1


def kruskal(n, edges):
    # Initialize the disjoint set
    ds = DisjointSet(n)
    mst = []  # To store the edges in the MST
    
    # Step 1: Sort edges by weight
    edges.sort(key=lambda x: x[2])  # Sort by edge weight (x[2] is the weight)
    
    # Step 2: Iterate over the edges
    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, weight))  # Add the edge to MST
        if len(mst) == n - 1:  # If we've added n-1 edges, we're done
            break
    
    return mst


# Example usage:
if __name__ == "__main__":
    n = 4  # Number of vertices
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
    
    mst = kruskal(n, edges)
    print("Minimum Spanning Tree (MST):")
    for u, v, weight in mst:
        print(f"Edge: {u}-{v}, Weight: {weight}")
