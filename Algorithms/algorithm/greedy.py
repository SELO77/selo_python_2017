__author__ = 'SELO77'


def find_best_station_and_covered_states(stations, states_needed):
	best_station = None
	covered_states = set()
	for station, states_for_station in stations.items():
		covered = states_for_station & states_needed
		if len(covered) > len(covered_states):
			best_station = station
			covered_states = covered
	return best_station, covered_states


def greedy():
	states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
	stations = {}
	stations['kone'] = set(['id', 'nv', 'ut'])
	stations['ktwo'] = set(['wa', 'id', 'mt'])
	stations['kthree'] = set(['or', 'nv', 'ca'])
	stations['kfour'] = set(['nv', 'ut'])
	stations['kfive'] = set(['ca', 'az'])

	final_stations = set()

	while states_needed:
		best_station, covered_states = find_best_station_and_covered_states(stations, states_needed)
		final_stations.add(best_station)
		states_needed -= covered_states
	return final_stations


def main():
	print(greedy())


if __name__ == '__main__':
	main()
	print('++END++')