__author__ = 'bharathramh'

import sys

WHITE = 255
GREY = 100
BLACK = 0

class BFS:

    def __init__(self, graph):
        self.graph = graph

    def BFS(self, graph, source):

        if source.status == False:
            return

        # Initialization
        for vertex in graph.vertexMap.values():
            vertex.color = WHITE
            vertex.d[0] = sys.maxsize
            vertex.pi = None
        vertex.color = GREY
        vertex.d[0] = sys.maxsize
        vertex.pi = None

        Q = []
        Q.append(source)

        while Q != None and len(Q) > 0:
            u = Q.pop(0)
            if u.status != True:
                continue
            for edge in graph.vertexMap[u.name].adj:
                # if edge.status == True:
                if edge.status == True and edge.destination.color == WHITE:
                    edge.destination.color = GREY
                    edge.destination.d[0] = u.d[0] + 1
                    edge.destination.pi = u
                    Q.append(edge.destination)
            # print("\t\t", u.name)
            u.color = BLACK

    def updataGraph(self, graph):
        self.graph = graph

    def printReachableVerticesFromAllSource(self):
        # data = sorted(self.graph.vertexMap.values(), key= lambda x : x.name)
        for current in self.graph.vertexMap.values():
            self.BFS(self.graph, current)
            if current.status != True:
                continue
            print(current.name)
            # _data = sorted(self.graph.vertexMap.values(), key= lambda x : x.name)
            for x in self.graph.vertexMap.values():
                if x.color != WHITE and x.status == True and x.name != current.name:
                    print("  ", x.name)
            # self.printPathFor(source)

    # def printPathFor(self, source):