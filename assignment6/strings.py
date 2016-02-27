"""String Split

Author: Travis Barnes 27 Feb, 2016 for CIS 315

Using two algorithms (iterative and recursive memoized), the program will search a
single string containing various words. It will then return whether or not the
string can be split into individual words (words are compared to a dictionary).
If the string can be split, the words will be output.
"""

import sys

def open_dict():
	"""Opens the dictionary file."""

	filename = 'diction10k.txt'

	try:
		target = open(filename, 'r')
		print("File opened.")
	except:
		print("Dictionary not found. Please make sure it is located in the same" 
			+ " folder as strings.py")


def open_string_file():
	"""Opens the user specified file containing the strings."""

	with open(sys.argv[1], 'r') as my_file:
		print(my_file.read())


if __name__ == "__main__":
	open_dict()
	open_string_file()
