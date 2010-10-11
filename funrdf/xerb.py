#!/usr/bin/env python
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.api import users
from models import StateStorage
from util import jsonDumps
from util.homepage import html
from xerblin.base import interpret


class MainHandler(webapp.RequestHandler):

    def get(self, state_key=None):
        user, state = self._preamble(state_key)
        if not user:
            return
        message = jsonDumps(state)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(message)

    def post(self, state_key=None):
        user, state = self._preamble(state_key)
        if not user:
            return

        command = self.request.get("command").split()
        next_state = interpret(state, command)
        state_key = StateStorage.store(user, next_state)

        message = jsonDumps(next_state)
        self.response.set_status(201)
        self.response.headers['Content-Location'] = state_key
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(message)

    def _preamble(self, state_key):

        # No state_key means the URL didn't include one.
        if not state_key: # Return some sensible homepage.
            self.response.out.write(html)
            return None, None

        user = users.get_current_user()
        assert user # This should be guarded in app.yaml.

        # Retrieve state.
        state = StateStorage.fetch(user, state_key)
        if not state:
            self._noStateError(state_key)
            return None, None

        return user, state

    def _noStateError(self, state_key):
        self.error(404)
        self.response.out.write(
            '404 <br>\n'
            'No such state: %s'
            % (state_key,)
            )


def main():
    application = webapp.WSGIApplication(
        [
            ('/xerblin/(.{,512})', MainHandler),
            ('/xerblin', MainHandler),
            ],
        debug=True,
        )
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
