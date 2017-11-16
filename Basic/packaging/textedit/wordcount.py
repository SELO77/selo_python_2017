def word_count(file_name):
	with open(file_name, 'r') as f:
		f_c = f.read()
		print('Word Count:', len(f_c.split()))


def sentence_count(file_name):
	with open(file_name, 'r') as f:
		f_c = f.read()
		print('Total Sentences:', f_c.count('.'))


if __name__ == '__main__':
	word_count('alice.txt')
	sentence_count('alice.txt')
