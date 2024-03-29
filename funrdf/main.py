#!/usr/bin/env python
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from util.homepage import html


class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write(html)


class MachineHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write(html)


def main():
    application = webapp.WSGIApplication(
        [
            ('/', MainHandler),
            ('/mech', MachineHandler),
            ],
        debug=True,
        )
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
