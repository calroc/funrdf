

CLOSING_TAGS =  set(['a', 'abbr', 'acronym', 'address', 'applet',
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
            'td', 'tfoot', 'th', 'thead', 'tr'])


NON_CLOSING_TAGS = set(['area', 'base', 'basefont', 'br', 'col', 'frame',
            'hr', 'img', 'input', 'isindex', 'link',
            'meta', 'param'])


# whitespace-insensitive tags, determines pretty-print rendering
LINE_BREAK_AFTER = NON_CLOSING_TAGS | set(['html','head','body',
    'frameset','frame',
    'title','script',
    'table','tr','td','th','select','option',
    'form',
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    ])


# tags whose opening tag should be alone in its line
ONE_LINE = set(['html','head','body',
    'frameset'
    'script',
    'table','tr','td','th','select','option',
    'form',
    ])


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
        res = []
        w = res.append

        if self.__class__.__name__ != "TEXT":
            res.extend(self._writeTag())

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

        return "".join(res)

    def _writeTag(self):

        yield "<%s" % self.tag

        # Attributes which will produce arg = "val"
        for k, v in self.attrs.iteritems():
            if not isinstance(v, bool):
                yield ' %s="%s"' % (k, v)

        # Attributes with no argument
        # If value is False, don't generate anything.
        # We test 'v is True' because we want only Booleans.
        for k, v in self.attrs.iteritems():
            if v is True:
                yield ' %s' % k

        yield ">"

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


# create the classes
for tag in CLOSING_TAGS | NON_CLOSING_TAGS | set(['text']):
    exec("class %s(TAG): pass" % tag.upper())

    
if __name__ == '__main__':
    head = HEAD(TITLE('Test document'))
    body = BODY()
    body <= H1('This is a test document') + \
            'First line' + BR() + 'Second line' + \
            (DIV("Neat", Class='hairy') <= "Well!")
    print HTML(head + body)
