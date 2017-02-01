from bottle import route, run


@route('/')
def home():
    return 'It is not fancy.'

run()