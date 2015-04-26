__author__ = 'bharathramh'


class MinHeap:

    """This Method is for Object and key for which the heap has to built should be passed while initializing.
    Build heap method will be called once the object is instantiated.
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
        self.aHeapsize = len(self.data)
        loc_i = self.parent(self.aHeapsize -1)
        while loc_i>=0:
            self.min_heapify(loc_i)
            loc_i-=1
        return self.data

    def extractMin(self):                                                       #O(log(n))

        if self.aHeapsize < 1:
            return None

        min = self.data[0]

        self.data[0] = self.data[self.aHeapsize-1]

        self.aHeapsize -= 1
        if self.aHeapsize > 0:
            self.min_heapify(0)
        return min

    def heapDecreaseKey(self, node, newValue, setKeyFunction):
        """
        :param node: The object whose priority has to decreased
        :param newValue: The new value of the Key in the object
        :setKeyFunction sk: Key setter function in object
        :return: Boolean
        """
        if newValue >  self.key(node):                                             #new value should be smaller than the old one
            return False

        i = node.position                                                       #index
        setKeyFunction(newValue)
        while i > 0 and self.key(self.data[self.parent(i)]) > self.key(self.data[i]):
            self.data[self.parent(i)].position, self.data[i].position = self.data[i].position, self.data[self.parent(i)].position
            self.data[self.parent(i)], self.data[i] = self.data[i], self.data[self.parent(i)]
            i = self.parent(i)
        return True

    def __len__(self):
        return self.aHeapsize