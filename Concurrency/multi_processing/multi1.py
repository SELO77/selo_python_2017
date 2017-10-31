import collections
import multiprocessing
from time import time


def fib(n):
	if n < 2:
		return n
	return fib(n-1) + fib(n-2)

if __name__ == '__main__':
	# test_set = (33, 33, 33, 33, 7, 10, 4, 5, 35, 30, 30, 30, 
	# 	30, 20, 20, 20, 20, 33,)
	test_set = (33, 33, 33, 33, 33, 33, 33, 30, 30, 30, 
		30, 20, 20, 20, 20, 33, 33)
	test_log_text_format = 'Duration: {:0.3f}'

	## multi-process calculation fibonacci
	pool = multiprocessing.Pool()
	st = time()
	result = pool.map(fib, test_set)
	print('==multiprocessing==')
	print(tuple(result))
	print(test_log_text_format.format(time() - st))

	## sequential calculation fibonacci
	st = time()
	result = []
	for i in test_set:
		result.append(fib(i))
	print('==sequential==')
	print(tuple(result))
	print(test_log_text_format.format(time() - st))

