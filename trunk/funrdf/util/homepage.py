from webout import *
'''
Simple demonstration of the webout tool.

Build a page with a form.
'''


title = 'Fun with RDF'


head = HEAD(TITLE(title))

body = BODY()
body <= H1(title)
body <= '''

This is a simple project to explore RDF, Semantic Web technologies and
the Google App Engine.

'''


print HTML(head + body)
