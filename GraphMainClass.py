__author__ = 'bharathramh'


from Vertex import *
from Edges import *
from Graph import *
from Dijkstra import *
from MinHeap import *
from BFS import *

import sys

class main:
    """ Initial graph can be populated by providing a text file with source, destination, and transit_time.
    eg: Belk Grigg 1.2"""
    def __init__(self):
        graph = Graph()
        self.outFile = open("output", 'w')
        try:
            filename = sys.argv[1]
            f = open(filename, 'r')
            for line in f:
                split = line.split()
                graph.addEdge(split[0], split[1], split[2])
            f.close()
        except IndexError:
            print("Input file was not passed while calling the function")
        while(True):
            userInput = input().split()

            if userInput == None or len(userInput) == 0:
                continue

            command = userInput.pop(0)
            self.writeInFile(command)
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
                if len(userInput) != 3:
                    print("addedge takes exactly 3 arguments.\nUsage :addedge <source Vertex> "
                          "<destination Vertex> <transit time>")
                    continue
                tailvertex, headvertex, transit_time = userInput[0],userInput[1], userInput[2]
                graph.updateEdge(tailvertex, headvertex, transit_time)

            elif command == "deleteedge":
                if len(userInput) != 2:
                    print("addedge takes exactly 2 arguments.\nUsage :deleteedge <source Vertex> "
                          "<destination Vertex>")
                    continue
                tailvertex, headvertex = userInput[0],userInput[1]
                graph.deleteEdge(tailvertex, headvertex)

            elif command == "edgeup":
                if len(userInput) != 2:
                    print("edgeup takes exactly 2 arguments.\nUsage :edgeup <source Vertex> "
                          "<destination Vertex>")
                    continue
                tailvertex, headvertex = userInput[0],userInput[1]
                graph.upEdgeStatus(tailvertex, headvertex)

            elif command == "edgedown":
                if len(userInput) != 2:
                    print("edgedown takes exactly 2 arguments.\nUsage :edgedown <source Vertex> "
                          "<destination Vertex>")
                    continue
                tailvertex, headvertex = userInput[0],userInput[1]
                graph.downEdgeStatus(tailvertex, headvertex)

            elif command == "vertexup":
                if len(userInput) != 1:
                    print("vertexup takes exactly 1 argument.\nUsage :vertexup <Vertex name>")
                    continue
                vertex = userInput[0]
                graph.upVertexStatus(vertex)

            elif command == "vertexdown" :
                if len(userInput) != 1:
                    print("vertexdown takes exactly 1 argument.\nUsage :vertexdown <Vertex name>")
                    continue
                vertex = userInput[0]
                graph.downVertexStatus(vertex)

            elif command == "reachable":
                if len(userInput) != 0:
                    print("reachable wont take argument.\nUsage :reachable")
                    continue
                # BFS(graph).printReachableVerticesFromAllSource()
                self.graph = graph
                bfs = BFS(self.graph)
                self.printReachableVerticesFromAllSource(bfs)
            elif command == "path":
                if len(userInput) != 2:
                    print("vertexdown takes exactly 2 argument.\nUsage :path <source Vertex>"
                          " <destination Vertex>")
                    continue
                source, destination = userInput[0],userInput[1]
                dijkstra = Dijkstra()
                source, destination = dijkstra.minPath(graph, source, destination)
                self.str = ""
                if self.printPath(source, destination) == "":
                    self.str = "No path found from "+ source.name + " to "+ destination.name
                else:
                    self.str += (" %.2f" % round(destination.d, 2))
                print(self.str)
                self.writeInFile(self.str)
            elif command == "quit":
                sys.exit(0)
            else:
                print("Incorrect command. The following commands are available"
                      "\nprint\naddedge\nedgedown\nedgeup\nvertexdown\nvertexup\nreachable\npath")
                pass
        self.outFile.close()


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

    def printReachableVerticesFromAllSource(self, bfs):
        # for current in sorted(self.graph.vertexMap.values()):                                         #use this line if sorting while printing is not required
        for current in sorted(self.graph.vertexMap.values(), key = lambda x : x.name):                  #use this line if sorting while printing is required
            bfs.BFS(self.graph, current)                               #Running time will be O(V(V+E))
            if current.status != True:
                continue
            self.writeInFile(current.name)
            print(current.name)

            # for x in sorted(self.graph.vertexMap.values(), key = lambda x : x.name):                  #use this line if sorting while printing is not required
            for x in sorted(self.graph.vertexMap.values(), key = lambda x : x.name):                    #use this line if sorting while printing is required
                if x.color == BLACK and x.status == True and x.name != current.name:
                    out = "  " + x.name
                    print(out)
                    self.writeInFile(out)

if __name__ == '__main__':
    main()