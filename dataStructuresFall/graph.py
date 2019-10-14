# Unweighted Grapgh
class AdjNode():
    def __init__(self, value):
        self.data = value
        self.next= None

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {} #[None]*self.V
        for i in range(self.V):
            self.graph[i] = None

    def addEdge(self, src, dest):
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        # node = AdjNode(src)
        # node.next = self.graph[dest]
        # self.graph[dest] = node

    def print(self):
        for i in range(self.V):
            print(i, end=' ')
            temp = self.graph[i]
            while temp:
                print(temp.data, end= ' ')
                temp = temp.next
            print('\n')

    def bfs(self, start):
        print(start, end=' ')
        queue = []
        visited = [False]*self.V
        queue.append(start)
        visited[start] = True

        while queue:
            node = queue.pop(0)
            temp = self.graph[node]
            while temp:
                
                if visited[temp.data] == True:
                    temp = temp.next
                    continue
                print(temp.data, end = ' ')
                queue.append(temp.data)
                visited[temp.data] = True
                temp = temp.next

    def distance(self, start, find):
        # print(start, end=' ')
        queue = []
        visited = [False]*self.V
        queue.append(start)
        visited[start] = True
        dist = 0

        while queue:
            count = 0
            node = queue.pop(0)
            temp = self.graph[node]
            while temp:
                if temp.data == find:
                    dist += 1
                    return dist
                if visited[temp.data] == True:
                    temp = temp.next
                    continue
                # print(temp.data, end = ' ')
                queue.append(temp.data)
                visited[temp.data] = True
                temp = temp.next

            dist += 1

        return dist

    def topologicalSortUtil(self, i, visited, stack):
        visited[i] = True

        temp = self.graph[i]
        while temp:
            if not visited[temp.data]:
                self.topologicalSortUtil(temp.data, visited, stack)
            temp = temp.next

        # for j in range(len(self.graph[i])):
        #     if not visited[j]:
        #         self.topologicalSortUtil(j, visited, stack)

        stack.append(i)

    def topologicalSort(self):
        visited = [0]*self.V
        stack = []

        for i in range(len(visited)):
            if not visited[0]:
                self.topologicalSortUtil(i, visited, stack)

        for _ in range(len(stack)):
            print(stack.pop(), end = ' ')



gra = Graph(7)
gra.addEdge(0,1) 
gra.addEdge(0,4) 
gra.addEdge(1,2) 
gra.addEdge(1,3) 
gra.addEdge(1,4) 
gra.addEdge(2,3)
gra.addEdge(2,5) 
gra.addEdge(3,4)
gra.addEdge(5,6)
# gra.addEdge(4,0)
# gra.addEdge(4,3)
# gra.print()
# gra.bfs(0)
print(gra.distance(0,2))
gra.topologicalSort()
