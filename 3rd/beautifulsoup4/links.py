def get_links(url):
    import requests
    from bs4 import BeautifulSoup as soup
    result = requests.get(url)
    page = result.text
    doc = soup(page)
    links = [element.get('href') for element in doc.find_all('a')]
    return links


if __name__ == '__main__':
    import sys
    if not len(sys.argv) > 1:
        raise IndexError('Arguments should be given 2 more, given system arguments : %s' % len(sys.argv))

    for url in sys.argv[1:]:
        print('Links in', url)
        links = get_links(url)
        for num, link in enumerate(links, start=1):
            if link is None:
                continue
            print(num, link)
        print()



