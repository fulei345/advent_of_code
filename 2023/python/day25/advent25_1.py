# This does not work
import time
# Move crucible over map where we should minimize heat 
import heapq

iPair = tuple
 
# This class represents a directed graph using
# adjacency list representation
class Graph:
    def __init__(self, V: int): # Constructor
        self.V = V
        self.adj = [[] for _ in range(V)]
 
    def addEdge(self, u: int, v: int, w: int):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))
 
    # Prints shortest paths from src to all other vertices
    def shortestPath(self, src: int, edges_list, count_list):
        # My own list of edges with minus values
        #edges_list
        #count_list

        # Create a priority queue to store vertices that
        # are being preprocessed
        pq = []
        heapq.heappush(pq, (0, src))
 
        # Create a vector for distances and initialize all
        # distances as infinite (INF)
        dist = [float('inf')] * self.V
        dist[src] = 0
 
        while pq:
            # The first vertex in pair is the minimum distance
            # vertex, extract it from priority queue.
            # vertex label is stored in second of pair
            d, u = heapq.heappop(pq)
 
            # 'i' is used to get all adjacent vertices of a
            # vertex
            for v, weight in self.adj[u]:
                # If there is shorted path to v through u.
                if dist[v] > dist[u] + weight:
                    # Updating distance of v
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))

                    if (v, u) in edges_list:
                        count_list[edges_list.index((v,u))] += 1
                    elif (u, v) in edges_list:
                        count_list[edges_list.index((u,v))] += 1
                    else:
                        edges_list.append((v,u))
                        count_list.append(1)
        # Print shortest distances stored in dist[]
        #for i in range(self.V):
        #    print(f"{i} \t\t {dist[i]}")


class Node:
    def __init__(self, name: str, index: int):

        self.name: str = name
        self.index: int = index
        self.neighbors: list = []
        self.connection: list[bool] = []

    def add_neighbor(self, other):
        self.neighbors.append(other)
        self.connection.append(True)

    def __lt__(self, other):
        return self.index < other.index

    def __eq__(self, other):
        if other is None:
            return False 
        return self.name == other.name

def main(file: str) -> int:
    all_nodes: list[Node] = []
    all_edges: liste[tuple] = []
    with open(file) as f:
        liste : list[str] = f.read().splitlines()
        for i in range(len(liste)):
            line = liste[i].split(":")
            left = line[0]
            right = line[1].split()

            all_edges.extend(process_line(left, right, all_nodes))

    count_list = [0 for _ in all_edges]

    g = Graph(len(all_nodes))
    for edge in all_edges:
        (start, end) = edge
        g.addEdge(start, end, 1)
    
    for i in range(len(all_nodes)):
        g.shortestPath(i, all_edges, count_list)
    
    find_highest_update(count_list, all_edges, all_nodes)
    numb = find_loop(all_nodes)
    

    result = (len(all_nodes)-numb) * numb
    return result

def find_loop(all_nodes):
    work_list = {all_nodes[0].index}
    seen = set()
    while len(work_list) != 0:
        current = work_list.pop()
        seen.add(current)
        for i, n in enumerate(all_nodes[current].neighbors):
            if n.index not in seen and all_nodes[current].connection[i]:
                work_list.add(n.index)
    #bvb, hfx, jqt, ntq, rhn, and xhk.
    return len(seen)

def find_highest_update(count_list, all_edges, all_nodes):
    three_lowest = [-1, -1, -1]
    three_lowest_indexes = [-1, -1, -1]
    for i in range(len(count_list)):
        for k in range(3):
            if count_list[i] > three_lowest[k]:
                three_lowest.insert(k,count_list[i])
                three_lowest.pop()
                three_lowest_indexes.insert(k,i)
                three_lowest_indexes.pop()
                break

    for index in three_lowest_indexes:
        (start, end) = all_edges[index]
        start_node: Node = all_nodes[start]
        end_node: Node = all_nodes[end]
        for i, n in enumerate(start_node.neighbors):
            if n.index == end:
                start_node.connection[i] = False

        for i, n in enumerate(end_node.neighbors):
            if n.index == end:
                end_node.connection[i] = False

def process_line(left: str, right: list, all_nodes: list[Node]):
    # process right side first, 
    all_edges = []
    right_list = []
    for node in right:
        temp = Node(node, 0)
        if temp in all_nodes:
            index = all_nodes.index(temp)
            right_list.append(all_nodes[index])
        else:
            new_node = Node(node,len(all_nodes))
            right_list.append(Node(node,len(all_nodes)))
            all_nodes.append(new_node)

    temp = Node(left, 0)
    if temp in all_nodes:
        index = all_nodes.index(temp)
        for node in right_list:
            all_nodes[index].add_neighbor(node)
            node.add_neighbor(temp)
            all_edges.append((index,node.index))
    else:
        new_node = Node(left,len(all_nodes))
        all_nodes.append(new_node)
        for node in right_list:
            new_node.add_neighbor(node)
            node.add_neighbor(new_node)
            all_edges.append((new_node.index,node.index))
    return all_edges


if __name__ == "__main__":
    
    start = time.time()
    result = main("test25.txt")
    end = time.time()
    expected = 54
    assert result == expected, f"Expected {expected} but got {result}"
    print(end - start)

    start = time.time()
    result = main("input25.txt")
    end = time.time()
    expected = 7798
    assert result == expected, f"Expected {expected} but got {result}"
    print(end - start)