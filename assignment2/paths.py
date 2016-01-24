"""Assignment 2

Author: Travis Barnes, 23 January 2016

Finds the longest, shortest, and number of paths, given a file of nodes.
"""

import sys
sys.path.insert(0, 'files')

# COUNT = 0

def file_parse():
	"""Processes graph structures from user specified file."""

	filename = input("Enter the file path for your graph: ")
	target = open(filename, 'r')

	target_lines = [] 	# List of lines from target file
	
	i = 0
	for line in target:
		if i == 0:
			graph_count = int(line)
		elif i == 1:
			node_count = int(line)
		elif i == 2:
			edge_count = int(line)
		else:	
			target_lines.append(line.strip('\n'))
		i += 1

	return graph_create(target_lines, graph_count, node_count, edge_count)


def graph_create(line_list, graphs, nodes, edges):
	"""Creates graphs from parsed file.

	Keyword arguments:
	line_list 	-- a list of parsed file lines
	graphs 	-- total number of graphs
	nodes 	-- total number of nodes
	edges 	-- total number of edges
	"""
	graph_count = graphs
	node_count = nodes
	edge_count = edges
	lines = line_list
	graphs = []
	x = 0

	for i in range(graph_count):
		print("Graph number: {}".format(i+1))

		prev_node = lines[0].split()[0]
		edges = []
		graph = []
		nodes = {}
		shortest_count = float('inf')
		longest_count = -1
		path_count = 0

		for j in range(x, edge_count):
			curr_node = lines[j].split()[0]
			# print("Edge: {}".format(lines[j]))

			if curr_node == prev_node:
				edges.append(lines[j].split()[1])

			else:
				edges = []
				edges.append(lines[j].split()[1])
			
			prev_node = curr_node

			nodes[int(lines[j].split()[0])] = [shortest_count, longest_count, path_count], edges
		
		if j == edge_count-1 and i < graph_count-1:
			node_count = int(lines[j+1])
			x = edge_count + 2
			edge_count += 2 + int(lines[j+2])

		graph.append(nodes)
		graphs.append(graph)

	return graphs


def traverse(nodes, node, path_count, path_length):
	"""Traverses graphs to find longest/shortest paths and total paths.

	Keyword arguments:
	node -- A list of nodes
	"""
	path_length += 1
	
	# For any connected_node, traverse that node unless it's the last node
	for connected_node in node[1]:
		try:
			traverse(nodes, nodes[int(connected_node)], path_count, path_length)
			
		except:
			# Total paths
			nodes[1][0][2] += 1
		
			# Shortest path
			if path_length < nodes[1][0][0]:
				nodes[1][0][0] = path_length
				print("Shortest path: {} ".format(path_length))

			# Longest path
			if path_length > nodes[1][0][1]:
				nodes[1][0][1] = path_length
				print("Longest path: {} ".format(path_length))

			continue


def shortest_path(graph):
	"""Finds the shortest path in a graph

	Keyword arguments:
	graphs -- A graph list
	"""


def longest_path(graph):
	"""Finds the longest path in a graph

	Keyword arguments:
	graph -- A graph list
	"""


def total_paths(graph):
	"""Finds the total number of paths in a graph.

	Keyword arguments:
	graph -- A graph list
	"""


if __name__ == "__main__":
	# file_parse()
	# print(file_parse())
	# for graph in file_parse():
	graphs = file_parse()
	# count = 0
	# for graph in graphs 
	# print(graphs[0][0])
	# for graph in graphs:
	traverse(graphs[1][0], graphs[1][0][1], 0, 0, 0)
	# for graph in graphs:
		# print(graph[0], graph[0][1])
	# for graph in (file_parse()):
		# for nodes in graph:
	# print(file_parse()[0][0]['1'][0:3])
	# print(file_parse()[0][0]['1'][4])
	# print(file_parse()[0][0]['1'][3][1])
		# shortest_path(graph)
