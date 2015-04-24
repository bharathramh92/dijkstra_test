from Vertex import *
from Edges import *

__author__ = 'bharathramh'

class Graph:
    def __init__(self):
        self.vertexMap = {}

    def addEdge(self, sourceName, destinationName, transit_time):
        source = self.getVertex(sourceName)
        destination = self.getVertex(destinationName)
        source.addEdge(Edges(source, destination, float(transit_time)))
        destination.addEdge(Edges(destination, source, float(transit_time)))

    def addEdgeUniDirection(self, s, d, transit_time):
        s.addEdge(Edges(s, d, float(transit_time)))

    def updateEdge(self, source, destination, transit_time):
        s = self.getVertex(source)
        d = self.getVertex(destination)
        edge = s.getEdgeFromVertex(d)
        if edge != None:
            edge.transit_time = float(transit_time)
        else :
            self.addEdgeUniDirection(s, d, transit_time)

    def deleteEdge(self, source, destination):
        s = self.getVertex(source)
        d = self.getVertex(destination)
        s.deleteEdge(d)

    def toggleEdgeStatus(self, sourceName, destinationName):
        s = self.getVertex(sourceName)
        d = self.getVertex(destinationName)
        edge = s.getEdgeFromVertex(d)
        if edge != None:
            edge.status = not edge.status

    def toggleVertexStatus(self, _vertex):
        s = self.getVertex(_vertex)
        if s != None:
            s.status = not s.status

    def getVertex(self, vertexName):
        try:
            v = self.vertexMap.get(vertexName)
            if v == None:
                v = Vertex(vertexName)
                self.vertexMap[vertexName] = v
            return v
        except KeyError as e:
            print("Exception ", e)

    def __repr__(self):
        return "vertexMap :%s \n" %(str(self.vertexMap))

