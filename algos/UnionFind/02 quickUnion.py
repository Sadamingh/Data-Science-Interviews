class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x, y):
        root_X = self.find(x)
        root_Y = self.find(y)
        if root_X != root_Y:
            self.root[root_Y] = root_X

    def connected(self, x, y):
        return self.find(x) == self.find(y)
