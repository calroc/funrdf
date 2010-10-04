from webout import *

url_base = 'http://localhost:8080/xerblin/'

def it(key='d971428eb68b4c9b8bf060b1775cd0d8'):
    name = 'Run command against state ' + key
    head = HEAD(TITLE(name))
    body = BODY()
    body <= H1(name)

    div = DIV()
    div <= FORM(method="post", action=url_base + key) \
        <= TABLE() \
            <= (
                TR(TD(INPUT(name='command', Type='entry')))
                +
                TR(TD(INPUT(name='Run command', Type='submit')))
                )
    body <= div
    return str(HTML(head + body))


print it()

