"""Assignment 2

Author: Travis Barnes, 23 January 2016

Finds the longest, shortest, and number of paths, given a file of nodes.
"""

import sys
sys.path.insert(0, 'files')


def file_parse():
	"""Processes graph structures from user specified file.

	Returns:
	graph_create() -- List of graphs
	"""

	filename = input("Enter the file path for your graph: ")
	target = open(filename, 'r')

	target_lines = [] 	# List of lines from target file
	
	# Grab the graph count and node/edge count for the first graph
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


def graph_create(line_list, graph_count, node_count, edge_count):
	"""Create graphs from file_

	Keyword arguments:
	line_list 	-- a list of parsed file lines
	graph_count -- total number of graphs
	node_count 	-- total number of node
	edge_count 	-- total number of edge

	Returns:
	graphs -- List of graphs
	"""

	lines = line_list
	graphs = []
	x = 0

	# For each graph
	for i in range(graph_count):
		prev_node = lines[0].split()[0]
		edges = []
		graph = []
		nodes = {}
		shortest_count = float('inf')
		longest_count = -1
		path_count = 0

		# For each node in the graph, store it and its connected nodes in  'nodes'
		for j in range(x, edge_count):
			curr_node = lines[j].split()[0]

			if curr_node == prev_node:
				edges.append(lines[j].split()[1])

			else:
				edges = []
				edges.append(lines[j].split()[1])
			
			prev_node = curr_node

			# Initialize  nodes  values for current node and insert all connect nodes  'edges'
			nodes[int(lines[j].split()[0])] = [shortest_count, longest_count, path_count], edges
		
		# If the last node in the graph is reached, move to the next graph
		if j == edge_count-1 and i < graph_count-1:
			node_count = int(lines[j+1])
			x = edge_count + 2
			edge_count += 2 + int(lines[j+2])

		graph.append(nodes)
		graphs.append(graph)

	return graphs


def graph_traverse(nodes, node, path_count, path_length):
	"""Traverses graphs to find longest/shortest paths and total paths.

	Keyword arguments:
	nodes -- A list of nodes
	node  -- A single node from nodes
	path_count  -- Total amount of paths
	path_length -- Length of current path
	"""
	path_length += 1
	
	# For any connected_node, traverse that node unless it's the last node
	for connected_node in node[1]:
		try:
			graph_traverse(nodes, nodes[int(connected_node)], path_count, path_length)
			
		except:
			# Total paths
			nodes[1][0][2] += 1
		
			# Shortest path
			if path_length < nodes[1][0][0]:
				nodes[1][0][0] = path_length

			# Longest path
			if path_length > nodes[1][0][1]:
				nodes[1][0][1] = path_length

			continue
	print(nodes[1][0][2])

if __name__ == "__main__":
	graphs = file_parse()

	# print(graphs[0])
	# print(graphs[0][0])
	# print(graphs[0][0][0])
	# print(graphs[0][0][0][0])
	
	i = 1
	for graph in graphs:
		graph_traverse(graph[0], graph[0][1], 0, 0)

		print("Graph number: {}".format(i))
		print("Shortest path: {}".format(graph[0][1][0][0]))
		print("Longest path: {}".format(graph[0][1][0][1]))
		print("Number of paths: {}\n".format(graph[0][1][0][2]))

		i += 1
