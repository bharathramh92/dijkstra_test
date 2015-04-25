__author__ = 'bharathramh'


from Vertex import *
from Edges import *
from Graph import *
from Dijkstra import *
from MinHeap import *
from BFS import *

import sys

class main:

    def __init__(self):
        self.outFile = open("output", 'w')
        filename = sys.argv[1]
        f = open(filename, 'r')
        graph = Graph()
        for line in f:
            split = line.split()
            graph.addEdge(split[0], split[1], split[2])

        while(True):
            userInput = input().split()

            if userInput == None or len(userInput) == 0:
                continue

            command = userInput[0]
            if command == "print":
                for key,value in sorted(graph.vertexMap.items()):

                    if not graph.vertexMap[key].status:
                        key += " DOWN"
                    print(key)

                    self.writeInFile(key)
                    orderedAdj = sorted(value.adj, key = lambda x: x.destination.name)
                    for edge in orderedAdj :
                        s = ""
                        if not edge.status:
                            s = "DOWN"
                        self.writeInFile(("  %s %s %s" %(edge.destination.name, edge.transit_time, s)))
                        print("  %s %s %s" %(edge.destination.name, edge.transit_time, s))
                    self.writeInFile("")

            elif command=="addedge":
                tailvertex, headvertex, transit_time = userInput[1],userInput[2], userInput[3]
                graph.updateEdge(tailvertex, headvertex, transit_time)

            elif command == "deleteedge":
                tailvertex, headvertex = userInput[1],userInput[2]
                graph.deleteEdge(tailvertex, headvertex)

            elif command == "edgeup":
                tailvertex, headvertex = userInput[1],userInput[2]
                graph.upEdgeStatus(tailvertex, headvertex)

            elif command == "edgedown":
                tailvertex, headvertex = userInput[1],userInput[2]
                graph.downEdgeStatus(tailvertex, headvertex)

            elif command == "vertexup":
                vertex = userInput[1]
                graph.upVertexStatus(vertex)

            elif command == "vertexdown" :
                vertex = userInput[1]
                graph.downVertexStatus(vertex)

            elif command == "reachable":
                BFS(graph).printReachableVerticesFromAllSource()

            elif command == "path":
                source, destination = userInput[1],userInput[2]
                dijkstra = Dijkstra()
                source, destination = dijkstra.minPath(graph, source, destination)
                self.str = ""
                if self.printPath(source, destination) == "":
                    self.str = "No path found from "+ source.name + " to "+ destination.name
                else:
                    self.str += (" %.2f" % round(destination.d[0], 2))
                print(self.str)
                self.writeInFile(self.str)
            elif command == "quit":
                sys.exit(0)
            else:
                pass

    def printPath(self, source, destination):

        if destination == source:
            self.str += destination.name + " "
        elif destination.pi == None:
            return ""
        else:
            self.printPath(source , destination.pi)
            self.str += destination.name + " "

        return self.str

    def writeInFile(self, st):
        self.outFile.write(st + "\n")

def h():
    a = [5,40,8,6,20]
    hp = MinHeap(a, key = lambda x : x)
    print(hp.data)

if __name__ == '__main__':
    main()
    # h()