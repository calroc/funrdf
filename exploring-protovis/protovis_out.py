

template = '''
var graph_data = {
  nodes:[
%s
  ],
  links:[
%s
  ]
};
'''


def makeNodes(a):
    return '\n'.join(
        '    {nodeName:"%s", group:1},' % (
            u' '.join(node.splitlines())[:80]
            )
        for node in a
        )


def makeLinks(g, z):
    return '\n'.join(
        '    {source:%i, target:%i, value:1},' % (z[s], z[o])
        for s, _, o in g
        )


def _iterAllNodes(g):
    for s, p, o in g:
        yield s
        # yield p
        yield o


g = [
    ('a', 'p', 'c'),
    ('b', 'p', 'c'),
    ('c', 'p', 'd'),
    ]

def makeGraphData(g):

    # Get all subjects and objects.
    X = sorted(set(_iterAllNodes(g)))

    # Map nodes to indicies.
    Z = dict(
        (uri, i)
        for i, uri in enumerate(X)
        )

    nodes = makeNodes(X)
    links = makeLinks(g, Z)

    return template % (nodes, links)

