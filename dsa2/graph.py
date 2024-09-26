class Graph:
    def __init__(self , edges) -> None:
        self.edges = edges
        self.graph_dict = {}

        # converting the list of tuples into the dict for easy of understanding and using it 
        for start , end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]


    # in this we will find all the routes and the shortest routes
    def get_paths(self, start , end , path = []): # making it a recursive function
        path = path + [start]
        
        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return []
        
        paths = []

        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.get_paths(node , end , path)

                for p in new_path:
                    paths.append(p)

        return paths
    
    def get_shortest_path(self , start , end , path = []):
        path = path + [start]

        if start == end:
            return path
        
        if start not in self.graph_dict:
            return None
        
        shortest_path = None

        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node , end , path)

                if sp:
                    if shortest_path is None or len(sp)<len(shortest_path):
                        shortest_path = sp

        return shortest_path
                    
        

if __name__ == "__main__":

    routes = [
            ("Mumbai", "Paris"),
            ("Mumbai", "Dubai"),
            ("Paris", "Dubai"),
            ("Paris", "New York"),
            ("Dubai", "New York"),
            ("New York", "Toronto"),
        ]
    
    start = 'Mumbai'
    end = 'Toronto'
    
    graph = Graph(routes)
    print(graph.get_paths(start , end))
    print(graph.get_shortest_path(start , end))
