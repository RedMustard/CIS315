import fileinput

def open_string_file():
	"""Opens the user specified file containing the strings."""
	# print(sys.argv[-1])

	try:
		for line in fileinput.input():
			print line
		# filename = open(sys.argv[1], 'r')
		# target = raw_input()
		# target.readline()
		# filename = open(target, 'r')
		# print target
		# for item in target:
			# print item
		# print(target)
		# print "something"

	except:
		print("File not found. Please make sure you entered one " +
		 "and that it is spelled correctly.")
		# sys.exit(1)
	# parse_file(filename)

if __name__ == '__main__':
	open_string_file()
	# print "something"