"""String Split

Author: Travis Barnes 27 Feb, 2016 for CIS 315

Using two algorithms (iterative and recursive memoized), the program will search a
single string containing various words. It will then return whether or not the
string can be split into individual words (words are compared to a dictionary).
If the string can be split, the words will be output.
"""

import sys

DICTSET = set()	## Set to hold dictionary


def read_dict():
	"""Opens the dictionary file and stores the words into a hash set."""

	filename = 'diction10k.txt'
	
	try:
		target = open(filename, 'r')

	except:
		print("Dictionary not found. Please make sure it is located in the same" 
			+ " folder as strings.py")
		sys.exit(1)

	for line in target:
		DICTSET.add(line.strip())


def open_string_file():
	"""Opens the user specified file containing the strings."""

	try:
		filename = open(sys.argv[1], 'r')

	except:
		print("File not found. Please make sure you entered one " +
		 "and that it is spelled correctly.")
		sys.exit(1)
	parse_file(filename)


def parse_file(file):
	"""Parses the string file.

	Keyword arguments:
	file -- File to be parsed
	"""
	file_lines = []

	## For each line in the file, if it's not empty, store it
	for line in file:
		if len(line) > 1:
			file_lines.append(line.strip())
	
	run_algorithms(file_lines)


def run_algorithms(string_list):
	"""Calls the iterative and recursive string split algorithms.

	Keyword arguments:
	string_list -- List of strings from file
	"""
	string_count = int(string_list[0])

	for i in range(1, string_count+1):
		string = string_list[i]
		print("Phrase number: ", i)
		print(string, "\n")
		split_string = []
		memo = set()

		print("Iterative attempt:")
		if iterative_string_split(string, split_string) is True:
			print("YES, can be split.")
			print(print_string_list(split_string))
		else:
			print("NO, cannot be split.")

		split_string = []

		print("\nMemoized attempt:")
		if recursive_string_split(string, 0, split_string, memo) is True:
			print("YES, can be split.")
			split_string.reverse()
			print(print_string_list(split_string))

		else:
			print("NO, cannot be split.")

		print("\n")


def print_string_list(string_list):
	"""Prints a list of strings.

	Keyword arguments:
	string_list -- A list containing strings.
	"""
	final_string = ""

	for string in string_list:
		final_string += string + " "

	return final_string


def iterative_string_split(string, split_string):
	diff = 0
	isWord = [[False for i in range(len(string)+1)] for i in range(len(string)+1)]
	t = [[False for i in range(len(string)+1)] for i in range(len(string)+1)]

	for i in range(len(string)):
		for j in range(len(string)):
			diff = i+j

			if diff < len(string):
				if string[j:diff+1] in DICTSET:
					isWord[j][diff] = True
					t[j][diff] = j

				for k in range(j+1, diff+1):
					if isWord[j][k-1] is True and isWord[k][diff] is True:
						isWord[j][diff] = True
						t[j][diff] = k
						break

	## Store the split strings
	i = 0
	j = len(string)-1

	while i < j:
		k = t[i][j]

		if i == k:
			split_string.append(string[i:j+1])
			break
		split_string.append(string[i:k])
		i = k

	return isWord[0][len(string)-1]


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

	## Iterate through the rest of the substrings
	j = i
	while j < len(string):
		if string[i:j+1] in DICTSET:
			if recursive_string_split(string, j+1, store_list, memo_set):
				store_list.append(string[i:j+1])
				return True
		j += 1

	## Store already looked at false strings
	memo_set.add(i)
	return False 


if __name__ == "__main__":
	read_dict()
	open_string_file()
