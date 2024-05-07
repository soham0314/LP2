class Graph:
    def __init__(self, graph):
        self.visited = []
        self.queue = []
        self.graph = graph

    def bfs(self, node):
        print(node)
        if node not in self.visited:
            self.visited.append(node)

        if node in self.graph:
            for neighbour in self.graph[node]:
                if neighbour not in self.visited and neighbour not in self.queue:
                    self.queue.append(neighbour) 

        if self.queue:
            vertex = self.queue.pop(0)
            self.visited.append(vertex)
            self.bfs(vertex)
            
    def dfs(self,node):
        if node not in self.visited:
            print(node)
            self.visited.append(node)
            if node in self.graph:
                for neighbour in self.graph[node]:
                    self.dfs(neighbour)
                
def create_graph():
    graph = {}
    nodes = int(input("Enter the number of nodes: "))

    for i in range(nodes):
        node = input(f"Enter node {i + 1}: ")
        neighbors = input(f"Enter neighbors for node {node} (comma-separated, press Enter if none): ")
        graph[node] = neighbors.split(',')
    
    return graph


def main():
    while True:
        print("Options:")
        print("1. Create Graph")
        print("2. BFS")
        print("3. DFS")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            graph = create_graph()
        elif choice == "2":
            start_node = input("Enter the starting node: ")
            g = Graph(graph)
            print("Executing BFS search")
            g.bfs(start_node)
        elif choice == "3":
            start_node = input("Enter the starting node: ")
            g = Graph(graph)
            print("Executing DFS search")
            g.dfs(start_node)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

main()