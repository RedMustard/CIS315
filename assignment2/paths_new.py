"""Paths - Resubmission

Author: Travis Barnes 11 Mar, 2016 for CIS 315

Finds the longest, shortest, and number of paths, given a file of nodes.
"""

import fileinput

def parse_stream():
	"""Parses the graph file via input stream."""
	file_lines = []

	file = fileinput.input()

	for line in file:
		if file.isfirstline():
			graph_count = int(line)

		for i in range(graph_count):
			# print("Graph number: ", i+1)
			try:
				node_count = int(next(file).strip())
				edge_count = int(next(file).strip())
			except:
				break

			edge_list = []

			for j in range(node_count):
				edge_list.append([])
				
			for x in range(1, edge_count*2, 2):
				index = next(file).strip().split()
				edge_list[int(index[0])].append(index[1])

			print("Graph number: ", i+1)
			print("Shortest Path: ", find_shortest_path(edge_list, node_count))
			print("Longest Path: ", find_longest_path(edge_list, node_count))
			print("Number of Paths: ", number_of_paths(edge_list, node_count), "\n")


def init_distance(size, n):
	"""Determines the distance [INSERT MORE HERE]

	Keyword arguments:
	size - (int) - total nodes
	n - (int) - distance
	"""
	distance = []

	for i in range(size+1):
		distance.append(n)

	return distance


def find_shortest_path(adjacency_list, size):
	"""

	Keyword arguments:
	adjacency_list - (list) - list of edges
	size - (int) - total nodes
	"""
	distance = init_distance(size, float('inf'))
	distance[1] = 0

	for i in range(1, size):
		edges = adjacency_list[i]

		for e in edges:
			if distance[int(e)] > distance[i] + 1:
				distance[int(e)] = distance[i] + 1

	return distance[size]


def find_longest_path(adjacency_list, size):
	"""

	Keyword arguments:
	adjacency_list - (list) - list of edges
	size - (int) - total nodes
	"""
	distance = init_distance(size, -1)
	distance[1] = 0

	for i in range(1, size):
		edges = adjacency_list[i]

		for e in edges:
			if distance[int(e)] < distance[i] + 1:
				distance[int(e)] = distance[i] + 1

	return distance[size]

def number_of_paths(adjacency_list, size):
	"""

	Keyword arguments:
	adjacency_list - (list) - list of edges
	size - (int) - total nodes
	"""
	path_count = init_distance(size, 0)
	path_count[1] = 1

	for i in range(1, size):
		edges = adjacency_list[i]

		for e in edges:
			path_count[int(e)] += path_count[i]

	return path_count[size]


if __name__ == "__main__":
	parse_stream()
