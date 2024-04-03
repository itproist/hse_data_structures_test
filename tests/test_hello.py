from main.hello import hello

def test_hello():
    name = 'me'
    assert hello(name) == 'Hello, me'
