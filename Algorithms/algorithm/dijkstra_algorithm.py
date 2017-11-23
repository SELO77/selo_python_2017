__author__ = 'SELO77'


from time import time


graph = {
	'START': {
		'A': 5,
		'B': 2
	},
	'A': {
		'C': 4,
		'D': 2,
	},
	'B': {
		'A': 8,
		'D': 7
	},
	'C': {
		'D': 6,
		'END': 3
	},
	'D': {
		'END': 1
	},
	'END': {}
}

INFINITY = float('inf')


def time_log(func):
	def wrapper(*args, **kwargs):
		st = time()
		result = func(*args, **kwargs)
		print("Execution Time: {0:8.2f}".format(time() - st))
		return result 
	return wrapper


def cached_result(func):
	def wrapper(*args, **kwargs):
		cache_key = str(kwargs.values())

		if func.__dict__.get(cache_key):
			print('Loaded cache on the {0}.'.format(func.__name__))
			return func.__dict__.get(cache_key)

		func.__dict__[cache_key] = func(*args, **kwargs)
		print('Cached result of {0}.'.format(func.__name__))
		return func.__dict__[cache_key]
	return wrapper


@cached_result
def neighbor_key(graph, start):
	return graph[start].keys()


def make_costs_table(graph, nodes_key, start='START'):	
	t = {}
	start_node_neighbor_key = neighbor_key(graph, start)
	for key in nodes_key:
		if key in start_node_neighbor_key:
			t[key] = graph[start][key]
		else:
			t[key] = INFINITY
	del t[start]
	return t 


def make_parents_table(graph, nodes_key, start='START'):
	t = {}
	start_node_neighbor_key = neighbor_key(graph, start)
	for key in nodes_key:
		if key in start_node_neighbor_key:
			t[key] = start
		else:
			t[key] = None
	del t[start]
	return t


def find_lowest_cost_node(graph, costs, processed):
	lowest_value = INFINITY
	lowest_key = None
	for k, v in costs.items():
		if k in processed:
			continue
		if v < lowest_value:
			lowest_value = v
			lowest_key = k
	return lowest_key

ARROW = '->'
make_path_result_format = '{0}%s{1}' % ARROW
def make_path(tict, start, end, result=''):
	prior_node = tict[end]
	if prior_node == start:
		return '{0}{arrow}{1}{arrow}{2}'.format(start, end, result, arrow=ARROW).rstrip(ARROW)
	result = make_path_result_format.format(end, result)
	return make_path(tict, start, prior_node, result=result)


@time_log
def search_shortest_path(graph, start='START', end='END'):
	nodes = graph.keys()
	costs = make_costs_table(graph, nodes)
	parents = make_parents_table(graph, nodes)
	processed = []

	node = find_lowest_cost_node(graph, costs, processed)
	while node is not None:
		processed.append(node)

		cost = costs[node]
		node_data = graph[node]

		for neighbor in node_data.keys():
			new_cost = cost + node_data[neighbor]

			if new_cost < costs[neighbor]:
				costs[neighbor] = new_cost
				parents[neighbor] = node

		node = find_lowest_cost_node(graph, costs, processed)
	return make_path(parents, start, end)


def main():
	global graph
	print(search_shortest_path(graph))


if __name__ == '__main__':
	main()
	print('++END++')