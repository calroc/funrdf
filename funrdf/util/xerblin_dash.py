from xerblin.library import words
from webout import *


def word2html(name, doc):
    head = HEAD(TITLE(name))
    body = BODY()
    body <= H1(name)
    if doc:
        doc = ' '.join(doc.split())
    else:
        doc = 'No documentation available.'
    body <= doc
    return str(HTML(head + body))


if __name__ == '__main__':
    for name, word in words:
        with open(name + '.html', 'w') as f:
            print >> f, word2html(name, word.__doc__)

