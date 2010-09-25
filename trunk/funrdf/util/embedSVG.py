from webout import *
'''
Support for embedding SVG graphics.
'''


# FIXME: These should be imported from a configuration module.
APP_URL = 'http://funrdf.appspot.com/'
SVG_DIR = 'static'


def embedSVG(filename, width=None, height=None):
    url = APP_URL + SVG_DIR + '/' + filename

    em = EMBED(src=url, type="image/svg+xml")
    if width is not None:
        em.attrs['width'] = str(width)
    if height is not None:
        em.attrs['height'] = str(height)

    return em + BR() + A('click here for full image', href=url)


if __name__ == '__main__':
    print embedSVG('EmailSignupModelFSM.svg', '460', '184')
