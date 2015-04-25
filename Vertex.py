__author__ = 'bharathramh'

import sys

class Vertex:
    """ Vertex class to store vertex details
    """
    def __init__(self, name):
        self.name = name
        self.adj = []
        self.status = True
        self.d = sys.maxsize
        self.pi = None
        self.reset()

    def setKeyForHeap(self, d):
        self.d = d

    def addEdge(self, edge):
        self.adj.append(edge)

    def getEdgeFromVertex(self, dest):
        for temp in self.adj:
            if dest == temp.destination:
                return temp
        return None

    def deleteEdge(self, dest):
        try:
            self.adj.remove(self.getEdgeFromVertex(dest))
        except ValueError as e:
            print("Edge not found ")

    def reset(self):
        self.dist = sys.maxsize
        self.prev = None

    def __repr__(self):
        return "\n\nVertex data \nname : %s adj : %s dist : %f status : %s prev : %s d: %s pi : %s"\
               %(self.name, self.adj, self.dist, self.status, self.prev, self.d, self.pi)






