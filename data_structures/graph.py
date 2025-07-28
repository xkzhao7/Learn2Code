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
            fn(node)
            visited.add(node)
            for neighbor in self.graph[node]:
                self.dfs(neighbor, visited)
    def bfs(self, source, fn=None, yield_nodes=False):
        visited = set()
        queue = LinkedList()
        queue.add(source)

        while queue.get_size() > 0:
            current = queue.remove(0)
            if current not in visited:
                if fn:
                    fn(current)
                elif yield_nodes:
                    yield current
                visited.add(current)
                for neighbor in self.graph[current]:
                    queue.add(neighbor)
    def has_path(self, node, destination):
        for value in self.bfs(node, yield_nodes=True):
            if value == destination:
                return True
        return False
        # non-generator method
        # if visited is None:
        #     visited = set()
        # if node not in visited:
        #     if node == destination:
        #         return True
        #     visited.add(node)
        #     for neighbor in self.graph[node]:
        #         if self.has_path(neighbor, destination, visited):
        #             return True
        # return False
if __name__ == "__main__":
    g = Graph()

    g.add_node("F")
    g.add_node("G")
    g.add_node("I")
    g.add_node("H")
    g.add_node("J")
    g.add_node("K")

    g.add_edge("F", "G")
    g.add_edge("F", "I")
    g.add_edge("I", "G")
    g.add_edge("I", "K")
    g.add_edge("G", "H")
    g.add_edge("J", "I")

    print(g.has_path("F", "K"))