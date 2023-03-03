class UnionFind:
    def __init__(self, n) -> None:
        self.parent = {}
        self.rank = {}

        for i in range(1, n + 1):
            self.parent[i] = i
            self.rank[i] = 0
    
    def find(self, n):
        parent = self.parent[n]
        while parent != self.parent[parent]:
            # This is where the path compression optimisation comes in
            self.parent[parent] = self.parent[self.parent[parent]]
            parent = self.parent[parent]
        return parent
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        # Here is the union by rank optimisation
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
        return True

