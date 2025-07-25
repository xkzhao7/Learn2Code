from linkedlist import LinkedList

class Graph:
    def __init__(self):
        self.graph = {}
    def add_node(self, node):
        self.graph[node] = set()
    def add_edge(self, node1, node2, directed=True):
        self.graph[node1].add(node2)
        if not directed:
            self.graph[node2].add(node1)
    def dfs(self, node, visited=None, fn=print):
        if visited is None:
            visited = set()
        if node not in visited:
            print(node)
            visited.add(node)
            for neighbor in self.graph[node]:
                self.dfs(neighbor, visited)
    def bfs(self, source, fn=print):
        visited = set()
        queue = LinkedList()
        queue.add(source)

        while queue.get_size() > 0:
            current = queue.remove(0)
            if current not in visited:
                print(current)
                visited.add(current)
                for neighbor in self.graph[current]:
                    queue.add(neighbor)

if __name__ == "__main__":
    g = Graph()

    g.add_node("A")
    g.add_node("B")
    g.add_node("C")
    g.add_node("D")
    g.add_node("E")
    g.add_node("F")
    g.add_node("G")

    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("B", "E")
    g.add_edge("C", "F")
    g.add_edge("C", "G")

    g.dfs("A")
    print("")
    g.bfs("A")