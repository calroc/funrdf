#!/usr/bin/env python
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.api import users
from util.homepage import html


class MainHandler(webapp.RequestHandler):
    def get(self, foo=None, bar=None):
        user = users.get_current_user()

        message = '<br>\n'.join(map(str, (
            foo,
            bar,
            user.nickname(),
            user.email(),
            user.user_id(),
            self.request.path,
            )))

        self.response.out.write(message)


def main():
    application = webapp.WSGIApplication(
        [
            ('/xerblin/(.*)', MainHandler),
            ('/xerblin', MainHandler),
            ],
        debug=True,
        )
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
