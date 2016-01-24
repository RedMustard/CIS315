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
		print("Graph number: {}".format(i+1))

		prev_node = target_lines[0].split()[0]
		edges = []
		graph = []
		nodes = {}

		for j in range(x, edge_count):
			curr_node = target_lines[j].split()[0]
			print("Edge: {}".format(target_lines[j]))

			if curr_node == prev_node:
				edges.append(target_lines[j].split()[1])

			else:
				edges = []
				edges.append(target_lines[j].split()[1])
			
			prev_node = curr_node

			nodes[target_lines[j].split()[0]] = edges
		
		if j == edge_count-1 and i < graph_count-1:
			node_count = int(target_lines[j+1])
			x = edge_count + 2
			edge_count += 2 + int(target_lines[j+2])

		graph.append(nodes)
		graphs.append(graph)

	# for graph in graphs:
		# print("Graph: {}".format(graph))

		# for graph in graphs:
	# for nodes in graphs[0]:
	# 	for val in nodes['1']:
	# 		print(val)
		# print(nodes['1'][0])


if __name__ == "__main__":
	file_process()
