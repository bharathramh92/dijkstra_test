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
        return (i-1)//2

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*i+2

    def min_heapify(self,i):

        l=self.left(i)
        r=self.right(i)
        smallest=i

        # print("data size %s l %s r %s i %s" %(len(self.data), l, r, i))
        # for x in self.data:
        #     print("current data " , x.name)

        if l<=self.aHeapsize :
            if self.key(self.data[l])<self.key(self.data[i]):
                smallest=l
                self.data[l].position = i
                self.data[smallest].position = l
            else:
                self.data[l].position = l
                self.data[smallest].position = i
        else:
            self.data[smallest] = i

        if r<=self.aHeapsize:
            if self.key(self.data[r])<self.key(self.data[smallest]):
                smallest=r
                self.data[r].position = smallest
                self.data[smallest].position = r
            else:
                self.data[r].position = r
                self.data[smallest].position = smallest
        else:
            self.data[smallest] = i
        # if smallest<=self.aHeapsize : self.data[smallest].position = smallest
        # if l<=self.aHeapsize : self.data[l].position = l
        # if r<=self.aHeapsize: self.data[r].position = r

        if smallest != i:
            self.data[smallest],self.data[i]=self.data[i],self.data[smallest]
            self.min_heapify(smallest)


    def build_heap(self):                                                       #O(n)
        # print("key is ", key)
        self.aHeapsize = len(self.data) -1
        loc_i=len(self.data)//2 -1
        while(loc_i>=0):
            self.min_heapify(loc_i)
            loc_i-=1
        # for x in self.data:
        #     try:
        #         x.position
        #     except Exception as e:
        #         print("position not assigned ",e, x.name)
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

        print("outside i is ", i)
        setKeyFunction(newValue)
        print("data size %s parent %s" %(len(self.data),self.parent(i)))
        while i > 0 and self.key(self.data[self.parent(i)]) < self.key(self.data[i]):
            self.data[self.parent(i)], self.data[i] = self.data[i], self.data[self.parent(i)]
            i = self.parent(i)
            print("inside")