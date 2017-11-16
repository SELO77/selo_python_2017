"""
This program takes a file as sys.arg[1] as input and returns a wordcount, character count ...
"""
print('wordcount_v2.py, __name__: ', __name__)
import re
import sys


class WC:
	def __init__(self, file_name):
		self.file_name = file_name

	def open_file(self, file_name):
		with open(file_name, 'r') as f:
			file_contents = f.read()
			return file_contents

	def word_count(self):
		wc_file = self.open_file(self.file_name)
		wc_word_list = wc_file.split()
		wc_word_count = len(wc_word_list)
		self = wc_word_count
		return ("Words Count: ", wc_word_count)

	def sentence_count(self):
		sc_file = self.open_file(self.file_name)
		return ("Sentences: ", sc_file.count('.'))

	def counts(self):
		print(self.word_count(), '\n', self.sentence_count(), '\n')


if __name__ == '__main__':
	try:
		alice = WC(sys.argv[1])
	except IndexError:
		print('Stupid Boy. Give me file_name!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
		exit(0)
	print(WC)
	print('+++')
	print(WC.counts(alice))
