class Heaps :
    def __init__(self):
        self.heaplist  = [0]
        self.currentsize = 0


 # parent of current node can be calculated by dividing index of current node by 2.
 # for every node , the value in parent is less than the value in the node
 # if node is at positon p , children are at poition 2p & 2p +1
    def adjust_heap(self , index) :
        while( index > 0) :
            if self.heaplist[i] < self.heaplist[i//2] :
                temp = self.heaplist[i//2]
                self.heaplist[i//2] = self.heaplist[i]
                self.heaplist[i] = temp
            index = index//2

    def insert(self,value):
        self.heaplist.append(value)
        self.currentsize = currentsize + 1
        self.adjust_heap(self.currentsize)

    def find_min_child(self,index):
        if 2*index +1 > self.currentsize :
            return 2* index
        if self.heaplist[2*index] < self.heaplist[2*index +1] :
            return 2*index
        else :
            return 2*index + 1

    def adjust_heap_down(self,index):
        while 2*index < self.currentsize :
            min_index  = find_min_child(index)
            if self.heaplist[index] > self.heaplist[min_index]
               temp = self.heaplist[index]
               self.heaplist[index] = self.heaplist[min_index]
               self.heaplist[min_index] = temp
            index = min_index

    def pop_min(self):
        val  = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentsize]
        self.currentsize = self.currentsize - 1
        self.heaplist.pop()
        adjust_heap_down(1)
        return val
