"""String Split

Author: Travis Barnes 27 Feb, 2016 for CIS 315

Using two algorithms (iterative and recursive memoized), the program will search a
single string containing various words. It will then return whether or not the
string can be split into individual words (words are compared to a dictionary).
If the string can be split, the words will be output.
"""

import sys

DICTSET = set()


def read_dict():
	"""Opens the dictionary file and stores the words into """

	filename = 'diction10k.txt'
	
	try:
		target = open(filename, 'r')
		print("File opened.")
	except:
		print("Dictionary not found. Please make sure it is located in the same" 
			+ " folder as strings.py")
		sys.exit(1)

	for line in target:
		DICTSET.add(line.strip())


def open_string_file():
	"""Opens the user specified file containing the strings."""

	filename = open(sys.argv[1], 'r')

	parse_file(filename)


def parse_file(file):
	"""Parses the string file.

	Keyword arguments:
	file -- File to be parsed
	"""
	file_lines = []

	for line in file:
		if len(line) > 1:	## Skip any empty lines
			file_lines.append(line.strip())
	
	string_count = int(file_lines[0])

	for i in range(1, string_count+1):
		string = file_lines[i]
		print("Phrase number: ", i)
		print(string, "\n")
		test = []
		memo = set()

		print("Iterative attempt: \n")
		iterative_string_split(string)

		print("Memoized attempt:")
		if recursive_string_split(string, 0, test, memo) is True:
			print("YES, can be split.")
			test.reverse()
			print(test)
		else:
			print("NO, cannot be split.")

		print("\n")


def iterative_string_split(string):
	"""Iterative algorithm for splitting a string into words.

	Keyword arguments:
	string - String to be split.
	"""


def recursive_string_split(string, i, store_list, memo_set):
	"""Recursive memoized algorithm for splitting a string into words.

	Keyword arguments:
	string - String to be split.
	"""
	## Base Case
	if string[i:] in DICTSET:
		store_list.append(string[i:])
		return True

	## Disregard strings already looked at
	if i in memo_set:
		return False

	j = i
	while j < len(string):
		
		if string[i:j+1] in DICTSET:
			if recursive_string_split(string, j+1, store_list, memo_set):
				store_list.append(string[i:j+1])
				return True
		j += 1

	memo_set.add(i)
	return False 


if __name__ == "__main__":
	read_dict()
	open_string_file()
