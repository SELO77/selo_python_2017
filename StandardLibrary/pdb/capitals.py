def process_cities(filename):
    with open(filename, 'rt') as f:
        for line in f:
            line = line.replace('', '')
            if 'quit' == line.lower():
                return
            try:
                country, city = line.split(',')
            except Exception as e:
                print(e)
                # TDOO: logging line number and detail which is occured error
                continue
            city = city.strip()
            country = country.strip()
            print(city.title(), country.title(), sep= ',')


if __name__ == '__main__':
    import sys
    print('load ', sys.argv[1])
    process_cities(sys.argv[1])

