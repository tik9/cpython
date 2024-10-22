# Dijkstra's shortest path algorithm
# adjacency matrix representation
def main():
    '''main'''
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
            [4, 0, 8, 0, 0, 0, 0, 11, 0],
            [0, 8, 0, 7, 0, 4, 0, 0, 2],
            [0, 0, 7, 0, 9, 14, 0, 0, 0],
            [0, 0, 0, 9, 0, 10, 0, 0, 0],
            [0, 0, 4, 14, 10, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 1, 6],
            [8, 11, 0, 0, 0, 0, 1, 0, 7],
            [0, 0, 2, 0, 0, 0, 6, 7, 0]
            ]

    g.dijkstra(0)

class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]

	# shortest path
	def dijkstra(self, src):

		dist = [1e7] * self.V
		dist[src] = 0
		sptSet = [False] * self.V

		for cout in range(self.V):

			# minimum distance vertex from set of vertices not yet processed.
			# u equal to src in first iteration
			# u = self.minDistance(dist, sptSet)
			# Initialize high minimum distance for next node
			min = 1e7

			# Search not nearest vertex not in shortest path tree
			for v in range(self.V):
				if dist[v] < min and sptSet[v] == False:
					min = dist[v]
					u = v

			# minimum distance vertex
			sptSet[u] = True

			# Update dist value of adjacent vertices of picked vertex if current distance greater than new distance and vertex not in shortest path tree
			for v in range(self.V):
				if (self.graph[u][v] > 0 and
				sptSet[v] == False and
				dist[v] > dist[u] + self.graph[u][v]):
					dist[v] = dist[u] + self.graph[u][v]

		print("Vertex \t Distance from Source")
		for node in range(self.V):
			print(node, "\t\t", dist[node])


if __name__=='__main__':
	main()