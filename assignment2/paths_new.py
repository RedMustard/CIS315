"""Paths - Resubmission

Author: Travis Barnes 11 Mar, 2016 for CIS 315

Finds the longest, shortest, and number of paths, given a file of nodes.
"""

import fileinput

def parse_file():
	"""Parses the string file."""
	file_lines = []

	file = fileinput.input()
	# graph_count = file[0]

	for line in file:
		# print(file.lineno())

		if file.isfirstline():
			graph_count = int(line)
			# print(next(file))

		for i in range(graph_count):
			print("Graph number: ", i+1)
			node_count = int(next(file).strip())
			edge_count = int(next(file).strip())

			a = []

			for j in range(node_count):
				a.append([])
				
			for x in range(edge_count):
				index = next(file).strip().split()
				a[int(index[0])-1].append(index[1])


if __name__ == "__main__":
	parse_file()
