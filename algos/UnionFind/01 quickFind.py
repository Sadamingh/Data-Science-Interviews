class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        return self.root[x]

    def union(self, x, y):
        root_X = self.find(x)
        root_Y = self.find(y)
        if root_X != root_Y:
            for i in range(len(self.root)):
                if self.root[i] != root_X:
                    self.root[i] = root_X

    def connected(self, x, y):
        return self.find(x) == self.find(y)
