"""Assignment 2

Author: Travis Barnes, 23 January 2016

Finds the longest, shortest, and number of paths, given a file of nodes.
"""

import sys
sys.path.insert(0, 'files')


def file_process():
	"""Takes user specified file and parses it.

	Keyword arguments:
	filename -- Name of user specified file
	"""

	filename = input("Enter the file path for your graph: ")
	target = open(filename, 'r')

	target_lines = []
	graphs = []
	graph = []
	node = {}
	edges = []

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

	x = 0	
	for i in range(graph_count):
		print("Graph Count: {} {}".format(graph_count, i))
		print("Edgecount: {}".format(edge_count))

		for j in range(x, edge_count):
			print("Edge: {}".format(target_lines[j]))
			# if j == 0:
			# 	nodes[target_lines[j].split()[0]] = target_lines[j].split()[1]
			# 	edges.append
			# else:
			# 	nodes[target_lines[j].split()[0]] += target_lines[j].split()[1]
			# # edges.append(int(target_lines[j]))
			# print(nodes)
		
		if j == edge_count-1 and i < graph_count-1:
			node_count = int(target_lines[j+1])
			x = edge_count + 2
			edge_count += 2 + int(target_lines[j+2])

		# graphs.append(graph)




def create_graph(graph_count, list):
	"""Dynamically creates graphs 

	Keyword arguments:
	count -- Number of graphs
	list  -- List of graph 
	"""


if __name__ == "__main__":
	file_process()
