__author__ = 'bharathramh'

import sys

WHITE = 255
GREY = 100
BLACK = 0

class BFS:

    def __init__(self, graph):
        self.graph = graph

    def BFS(self, graph, source):                                       #Running of BFS will be O(V+E)
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
            u = Q.pop(0)
            if u.status != True:
                continue
            for edge in graph.vertexMap[u.name].adj:

                if edge.status == True and edge.destination.color == WHITE:
                    edge.destination.color = GREY
                    edge.destination.d = u.d + 1
                    edge.destination.pi = u
                    Q.append(edge.destination)
            u.color = BLACK

    def updataGraph(self, graph):
        self.graph = graph

    def printReachableVerticesFromAllSource(self):
        # for current in sorted(self.graph.vertexMap.values()):                                         #use this line if sorting while printing is not required
        for current in sorted(self.graph.vertexMap.values(), key = lambda x : x.name):                  #use this line if sorting while printing is required
            self.BFS(self.graph, current)                               #Running time will be O(V(V+E))
            if current.status != True:
                continue
            print(current.name)

            # for x in sorted(self.graph.vertexMap.values(), key = lambda x : x.name):                  #use this line if sorting while printing is not required
            for x in sorted(self.graph.vertexMap.values(), key = lambda x : x.name):                    #use this line if sorting while printing is required
                if x.color == BLACK and x.status == True and x.name != current.name:
                    print("  ", x.name)
