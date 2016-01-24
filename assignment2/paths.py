"""Assignment 2

Author: Travis Barnes, 23 January 2016

Finds the longest, shortest, and number of paths, given a file of nodes.
"""

import sys
sys.path.insert(0, 'files')


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

		for j in range(x, edge_count):
			curr_node = lines[j].split()[0]
			print("Edge: {}".format(lines[j]))

			if curr_node == prev_node:
				edges.append(lines[j].split()[1])

			else:
				edges = []
				edges.append(lines[j].split()[1])
			
			prev_node = curr_node

			nodes[lines[j].split()[0]] = edges
		
		if j == edge_count-1 and i < graph_count-1:
			node_count = int(lines[j+1])
			x = edge_count + 2
			edge_count += 2 + int(lines[j+2])

		graph.append(nodes)
		graphs.append(graph)

	return graphs

	# for graph in graphs:
		# print("Graph: {}".format(graph))

		# for graph in graphs:
	# for nodes in graphs[0]:
	# 	for val in nodes['1']:
	# 		print(val)
		# print(nodes['1'][0])


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

	l_path = []

	# # Initialize
	# LP[1]=0
	# for i = 2 to N: 
	# 	LP[i] = —infinity

	# # loop
	# for i = 1 to N-1:
	# 	for j=i+1 to N:
	# 		if (i,j) is an edge:
	# 			LP[j] = MAX[ LP[j], 1+LP[i]  ]
 #        		# (update other properties here, if any)
	# print()


def total_paths(graph):
	"""Finds the total number of paths in a graph.

	Keyword arguments:
	graph -- A graph list
	"""


if __name__ == "__main__":
	print(file_parse())
	# for graph in (file_parse()):
		# shortest_path(graph)
