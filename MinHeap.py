__author__ = 'bharathramh'


class MinHeap:

    """Build heap method will be called once the object is instantiated.
    updateData will also call the build heap method with the new data."""

    def __init__(self, data, key):
        self.data = data
        self.key = key
        self.build_heap()

    def updateData(self, data, key):
        self.data = data
        self.key = key
        self.build_heap(self.data)

    def parent(self, i):
        return (i+1)//2-1

    def left(self, i):
        return 2*i+1

    def right(self, i):
        return 2*i+1+1

    # def min_heapify(self, data,i, key):
    #
    #     l=self.left(i)
    #     r=self.right(i)
    #     smallest=i
    #
    #     if l<=self.aHeapsize and data[l]<data[i]:
    #         smallest=l
    #     if r<=self.aHeapsize and data[r]<data[smallest]:
    #         smallest=r
    #     if smallest != i:
    #         print("data smallest is ", data[smallest])
    #         data[smallest],data[i]=data[i],data[smallest]
    #         self.min_heapify(data,smallest)

    def min_heapify(self,i):

        l=self.left(i)
        r=self.right(i)
        smallest=i

        if l<=self.aHeapsize and self.key(self.data[l])<self.key(self.data[i]):
                smallest=l
        if r<=self.aHeapsize and self.key(self.data[r])<self.key(self.data[smallest]):
                smallest=r
        print("Index smallest : %s left : %s right : %s" %(smallest, l, r))
        # self.data[smallest].position = smallest
        # if l<=self.aHeapsize: self.data[l].position = l
        # if r<=self.aHeapsize: self.data[r].position = r
        if smallest != i:
            self.data[smallest],self.data[i]=self.data[i],self.data[smallest]
            self.min_heapify(smallest)


    def build_heap(self):                                                       #O(n)
        # print("key is ", key)
        self.aHeapsize = len(self.data) - 1
        loc_i=len(self.data)//2-1
        while(loc_i>=0):
            self.min_heapify(loc_i)
            loc_i-=1
        # for x in self.data:
        #     print("heap data :" , x.name)
        for x in self.data:
            print("position of %s : %s" % (x.name, x.position))
        return self.data

    def extractMin(self):                                                       #O(log(n))

        if self.aHeapsize < 0:
            return None

        min = self.data[0]
        # self.data.insert(0, self.data.pop(self.aHeapsize))
        if len(self.data) > 1:                                              #not possible to insert the last value to the first one directly
            self.data[0] = self.data.pop(self.aHeapsize)
        else:
            self.data.pop(self.aHeapsize)

        self.aHeapsize -= 1
        self.min_heapify(0)
        return min

    def heapDecreaseKey(self, node, setKeyFunction, newValue):
        if newValue >  self.key(node):                                             #new value should be smaller than the old one
            return None

        i = node.position                                                          #index
        print("i is ", i)
        setKeyFunction(newValue)
        while i > 0 and self.key(self.data[self.parent(i)]) < self.key(self.data[i]):
            print("i is ", i)
            self.data[self.parent(i)], self.data[i] = self.data[i], self.data[self.parent(i)]
            i = self.parent(i)
            print("i is ", i)