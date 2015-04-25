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

        if l<self.aHeapsize and self.key(self.data[l]) < self.key(self.data[i]):
            smallest=l

        if r<self.aHeapsize and self.key(self.data[r]) < self.key(self.data[smallest]):
            smallest=r

        if smallest != i:
            if smallest == l:
                if l<self.aHeapsize: self.data[l].position = i
                self.data[i].position = l
                if r<self.aHeapsize: self.data[r].position = r
            elif smallest == r:
                if r<self.aHeapsize: self.data[r].position = i
                self.data[i].position = r
                if l<self.aHeapsize: self.data[l].position = l

            self.data[smallest],self.data[i]=self.data[i],self.data[smallest]
            self.min_heapify(smallest)
        else:
            if l<self.aHeapsize: self.data[l].position = l
            self.data[i].position = i
            if r<self.aHeapsize: self.data[r].position = r


    def build_heap(self):                                                       #O(n)
        # print("key is ", key)
        self.aHeapsize = len(self.data)
        loc_i = self.parent(self.aHeapsize -1)
        while loc_i>=0:
            self.min_heapify(loc_i)
            loc_i-=1
        # self.markPosition()
        # print("size after build heap ", len(self.data))
        return self.data

    # def markPosition(self):
    #     for x in range(0, self.aHeapsize + 1, 1):
    #         print(x, " ", self.data[x].name)
    #         self.data[x].position = x

    def extractMin(self):                                                       #O(log(n))

        if self.aHeapsize < 1:
            return None

        # for x in self.data:
        #     print("data size is ", len(self.data),"d ", x.name, "values are " , x.d)
        min = self.data[0]
        # print("min is ", min.name)

        # print("data zero th %s data heap-1 %s" %(self.data[0].name, self.data[self.aHeapsize -1].name))
        self.data[0] = self.data[self.aHeapsize-1]

        # if len(self.data) > 1:                                              #not possible to insert the last value to the first one directly
        #     self.data[0] = self.data.pop(self.aHeapsize-1)
        # else:
        #     self.data.pop(self.aHeapsize-1)

        self.aHeapsize -= 1
        if self.aHeapsize > 0:
            self.min_heapify(0)
        # print("aHeapsize %s cur min name %s" %(self.aHeapsize, min.name))
        return min

    def heapDecreaseKey(self, node, newValue):
        if newValue >  self.key(node):                                             #new value should be smaller than the old one
            return None

        try:
            i = node.position
            # i = self.data.index(node)                                                         #index
            # print("index :", node.name, " is ", i)
            # settingKeyFunction[0] = newValue
            # decreaseKeyFn(node, newValue)

            # node.d = newValue
            while i > 0 and self.key(self.data[self.parent(i)]) > self.key(self.data[i]):
                self.data[self.parent(i)].position, self.data[i].position = self.data[i].position, self.data[self.parent(i)].position
                self.data[self.parent(i)], self.data[i] = self.data[i], self.data[self.parent(i)]
                i = self.parent(i)
        except Exception as e:
            print("Exception")
        #



    def __len__(self):
        return self.aHeapsize