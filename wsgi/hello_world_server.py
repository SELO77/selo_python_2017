try:
    from cgi import parse_qs, escape
except ImportError:
    from urllib.parse import parse_qs
    from html import escape


def hello_world(environ, start_response):
    parameters = parse_qs(environ.get('QUERY_STRING', ''))
    if 'subject' in parameters:
        subject = escape(parameters['subject'][0])
    else:
        subject = 'World'
    start_response('200 OK', [('Content-type', 'text/html')])
    # return [bytes('''Hello %(subject)s
    # Hello %(subject)s!
    # ''' % {'subject': subject})]
    return [bytes('''Hello %(subject)s
        Hello %(subject)s!
        ''' % {'subject': subject}, encoding='utf-8')]

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8009, hello_world)
    srv.serve_forever()

    # 1. request http://localhost:8009/?subject=SELO.
    # 2. response Hello SELO. Hello SELO.!
