print('replace.py, __name__: ', __name__)
from wordcount_v2 import WC


def replace_words(file_name, new_word='SELO SELO'):
	with open(file_name, 'r') as inpu:
		with open('texts/new_alice.txt', 'w') as output:
			for line in inpu:
				line = line.rstrip()
				newline = line.replace("Alice", new_word)
				print(newline)
				output.write(newline)


if __name__ == '__main__':
	alice_file_name = 'alice.txt'
	replace_words(alice_file_name)
	print()
	alice = WC(alice_file_name)
	alice_word_count = alice.word_count()
	print('alice after called word_count:', alice)
	new_alice = WC('texts/new_alice.txt')

	print("Old Wordcount:", alice.word_count())
	print("WC __name__", WC.__name__)
	print("New Wordcount:", new_alice.word_count())
	print("replace __name__:", __name__)
