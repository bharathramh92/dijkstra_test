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
            vertex.d = sys.maxsize
            vertex.pi = None
        source.color = GREY
        source.d = 0
        source.pi = None

        Q = []
        Q.append(source)

        while Q != None and len(Q) > 0:
            # print("Q has the size ", len(Q))
            # for x in Q:
            #     print(x.name, " is present in Q")
            u = Q.pop(0)
            if u.status != True:
                continue
            # print("total edges are ", len(graph.vertexMap[u.name].adj))
            for edge in graph.vertexMap[u.name].adj:
                # if edge.status == True:

                if edge.status == True and edge.destination.color == WHITE:
                    edge.destination.color = GREY
                    edge.destination.d = u.d + 1
                    edge.destination.pi = u
                    Q.append(edge.destination)
                    # print("appending ", edge.destination.name)
            # print("\t\t", u.name)
            u.color = BLACK

    def updataGraph(self, graph):
        self.graph = graph

    def printReachableVerticesFromAllSource(self):
        # data = sorted(self.graph.vertexMap.values(), key= lambda x : x.name)
        for current in self.graph.vertexMap.values():                           #Current vertex
            self.BFS(self.graph, current)
            if current.status != True:
                continue
            print(current.name)
            # _data = sorted(self.graph.vertexMap.values(), key= lambda x : x.name)
            for x in self.graph.vertexMap.values():
                # if x.color == GREY and x.status == True and x.name != current.name:
                #     print("  ", x.name, " is grey node")
                if x.color == BLACK and x.status == True and x.name != current.name:
                    print("  ", x.name)
            # self.printPathFor(source)

    # def printPathFor(self, source):