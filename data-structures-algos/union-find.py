class Quick_Union_Find:
    def __init__(self , n):
        self.union_array = []
        self.sz = [1]*n
        for i in range(n):
            self.union_array[i] = i

    # quick find technique
    # def is_connected(self,p1,p2):
    #     if self.union_array[p1] == self.union_array[p2]:
    #         return True
    #     else :
    #         return False
    #
    # def union(self,p1,p2):
    #     int v1 = self.union_array[p1]
    #     int v2 =  self.union_array[p2]
    #     for i in range(len(union_array)):
    #         if self.union_array[i] == v1 :
    #             self.union_array[i] = v2

    #quick union technique
    def find_root(self , value):
         while value != self.union_array[value]:
             value = self.union_array[value]
         return value
    #
    # def is_connected(self, p1,p2):
    #     if find_root(p1) == find_root(p2):
    #         return True
    #     else :
    #         return False
    #
    # def union(self,p1,p2):
    #     r1 = root(p1)
    #     r2 = root(p2)
    #     self.union_array[r1] = r2

    # quick union with  weights  . change root of  smallest sized tree to ensure flat structure
    # leads to lg N runtime for both union and connected ..
    def union(self,p1,p2):
        r1 = self.find_root(p1)
        r2  = self.find_root(p2)
        if self.sz[r1] > self.sz[r2] :
            self.sz[r1] += self.sz[r2]
            self.union_array[r2] = r1
        else :
            self.sz[r2] += self.sz[r1]
            self.union_array[r1] = r2

    # find root with compression ...greater performance improvment in theory
    def comp_root(self,p):
        while p != self.union_array[p] :
            self.union_array[p] = self.union_array[self.union_array[p]]
            p = self.union_array[p]
        return p
