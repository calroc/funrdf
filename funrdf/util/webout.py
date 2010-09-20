import cStringIO

class TAG:

    def __init__(self, inner_HTML="", **attrs):
        self.tag = self.__class__.__name__.lower()
        self.inner_HTML = inner_HTML
        self.attrs = dict(
            (k.replace('_','-').lower(), v)
            for k, v in attrs.iteritems()
            )
        self.children = []
        self.brothers = []
    
    def __str__(self):
        res = cStringIO.StringIO()
        w = res.write
        if self.__class__.__name__ != "TEXT":
            w("<%s" % self.tag)

            # attributes which will produce arg = "val"
            attr1 = [
                k
                for k, v in self.attrs.iteritems()
                if not isinstance(v, bool)
                ]
            w("".join(
                    ' %s="%s"' % (k, self.attrs[k])
                    for k in attr1
                    )
              )

            # attributes with no argument
            # if value is False, don't generate anything
            # We test 'v is True' because we want only Booleans.
            attr2 = [k for k, v in self.attrs.iteritems() if v is True]
            w("".join(' %s' % k for k in attr2))
            w(">")

        if self.tag in ONE_LINE:
            w('\n')

        w(str(self.inner_HTML))

        for child in self.children:
            w(str(child))

        if self.tag in CLOSING_TAGS:
            w("</%s>" % self.tag)

        if self.tag in LINE_BREAK_AFTER:
            w('\n')

        for brother in self.brothers:
            w(str(brother))

        return res.getvalue()

    def __le__(self, other):
        """Add a child"""
        if isinstance(other, str):
            other = TEXT(other)
        self.children.append(other)
        other.parent = self
        return self

    def __add__(self, other):
        """Return a new instance : concatenation of self and another tag"""
        res = TAG()
        res.tag = self.tag
        res.inner_HTML = self.inner_HTML
        res.attrs = self.attrs
        res.children = self.children
        res.brothers = self.brothers + [other]
        return res

    def __radd__(self, other):
        """Used to add a tag to a string"""
        if isinstance(other, str):
            t = TEXT(other)
            t.brothers.append(self)
            return t
        else:
            raise ValueError, "Can't concatenate %s and instance" % other

    def __mul__(self, n):
        """Replicate self n times, with tag first : TAG * n"""
        res = TAG()
        res.tag = self.tag
        res.inner_HTML = self.inner_HTML
        res.attrs = self.attrs
        for i in range(n - 1):
            res += self
        return res

    def __rmul__(self, n):
        """Replicate self n times, with n first : n * TAG"""
        return self * n

# list of tags, from the HTML 4.01 specification

CLOSING_TAGS =  ['a', 'abbr', 'acronym', 'address', 'applet',
            'b', 'bdo', 'big', 'blockquote', 'button',
            'caption', 'center', 'cite', 'code',
            'del', 'dfn', 'dir', 'div', 'dl',
            'em', 'fieldset', 'font', 'form', 'frameset',
            'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
            'i', 'iframe', 'ins', 'kbd', 'label', 'legend',
            'map', 'menu', 'noframes', 'noscript', 'object',
            'ol', 'optgroup', 'pre', 'q', 's', 'samp',
            'script', 'select', 'small', 'span', 'strike',
            'strong', 'style', 'sub', 'sup', 'table',
            'textarea', 'title', 'tt', 'u', 'ul',
            'var', 'body', 'colgroup', 'dd', 'dt', 'head',
            'html', 'li', 'p', 'tbody','option', 
            'td', 'tfoot', 'th', 'thead', 'tr']

NON_CLOSING_TAGS = ['area', 'base', 'basefont', 'br', 'col', 'frame',
            'hr', 'img', 'input', 'isindex', 'link',
            'meta', 'param']

# create the classes
for tag in CLOSING_TAGS + NON_CLOSING_TAGS + ['text']:
    exec("class %s(TAG): pass" % tag.upper())
    
def concatinate(iterable):
    """Return the concatenation of the instances in the iterable."""
    it = list(iterable)
    if it:
        return reduce(lambda x,y:x+y, it)
    else:
        return ''

# whitespace-insensitive tags, determines pretty-print rendering
LINE_BREAK_AFTER = NON_CLOSING_TAGS + ['html','head','body',
    'frameset','frame',
    'title','script',
    'table','tr','td','th','select','option',
    'form',
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    ]

# tags whose opening tag should be alone in its line
ONE_LINE = ['html','head','body',
    'frameset'
    'script',
    'table','tr','td','th','select','option',
    'form',
    ]

if __name__ == '__main__':
    head = HEAD(TITLE('Test document'))
    body = BODY()
    body <= H1('This is a test document') + \
            'First line' + BR() + 'Second line' + \
            (DIV("Neat", Class='hairy') <= "Well!")
    print HTML(head + body)
