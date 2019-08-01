import math

class node():
    def __init__(self, nodeId = 0, vertex = [], visited = False, cost = math.inf):
        self.nodeId = nodeId
        self.vertex = vertex
        self.visited = visited
        self.cost = cost

    def __repr__(self):
      return "({})".format(self.nodeId)

class vertex():
  def __init__(self, nodeTarget = None, distance = 1):
    self.nodeTarget = nodeTarget
    self.distance = distance

  def __repr__(self):
    return "{}={}".format(self.nodeTarget, self.distance)

# entrada: "a, b, c" onde a = idOrigem, b = idDestino, c = distancia de a para b
# origin = node(nodeId = a)
# target = node(nodeId = b)
# vertex(nodeOrigin = origin, nodeTarget = target, distance = c)

a, b, c, d = node(nodeId = "a"), node(nodeId = "b"), node(nodeId = "c"), node(nodeId = "d")

a.vertex.append(vertex(nodeTarget = b, distance = 5))
a.vertex.append(vertex(nodeTarget = c, distance = 6))
b.vertex.append(vertex(nodeTarget = d, distance = 2))
c.vertex.append(vertex(nodeTarget = d, distance = 2))

print(a.vertex)
