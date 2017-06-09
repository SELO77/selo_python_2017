import re

try:
    from cgi import parse_qs, escape
except ImportError:
    from urllib.parse import parse_qs
    from html import escape


HTTP_STATUS = {
    '200': '200 OK',
    '404': '404 NOT FOUND',
}

DEFAULT_HEADER = [('Content-Type', 'text/html')]


def str_to_byte(s=''):
    return bytes(s, encoding='utf-8')

def index(environ, start_response):
    start_response(HTTP_STATUS['200'], DEFAULT_HEADER)
    return [str_to_byte('''Hello World Application
               This is the Hello World application:
                `continue <hello/>`_
    ''')]

def hello(environ, start_response):
    # parameters = parse_qs(environ.get('QUERY_STRING', ''))
    # if 'subject' in parameters:
    #     subject = escape(parameters['subject'][0])
    # else:
    #     subject = 'World'
    args = environ.get('myapp.url_args')
    if args:
        subject = escape(args[0])
    else:
        subject = 'World'
    result = start_response(HTTP_STATUS['200'], DEFAULT_HEADER)
    return [bytes('''Hello %(subject)s
            Hello %(subject)s!
            ''' % {'subject': subject}, encoding='utf-8')]

def not_found(environ, start_response):
    start_response(HTTP_STATUS['404'], [('Content-Type', 'text/plain')])
    return [str_to_byte('Not Found')]

def raise_error(environ, start_response):
    raise SystemError("SELO's intentional Error for test exception-middleware.")

urls = [
    (r'^$', index),
    (r'hello/?$', hello),
    (r'hello/(.+)$', hello),
    (r'raise_error_test/?$', raise_error)
]

def application(environ, start_response):
    path = environ.get('PATH_INFO', '').lstrip('/')
    for regex, callback in urls:
        match = re.search(regex, path)
        if match is not None:
            environ['myapp.url_args'] = match.groups()
            return callback(environ, start_response)
    return not_found(environ, start_response)


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    from wsgi.middleware.middleware import ExceptionMiddleware
    srv = make_server('localhost', 8009, ExceptionMiddleware(application))
    try:
        print('Start running')
        srv.serve_forever()
    except KeyboardInterrupt:
        print('Stop running')
        exit()

    # request URL example: http://localhost:8009/hello/John123
