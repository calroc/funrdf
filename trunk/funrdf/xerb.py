#!/usr/bin/env python
import pickle
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.api import users
from models import StateStorage
from util import jsonDumps
from util.homepage import html
from xerblin.btree import fillTree, items, get
from xerblin.library import words
from xerblin.base import interpret

##k = StateStorage.store('1', (1, 2, 3))
##print k
##print 


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
        state_key = self.saveNextState(user, next_state)

        message = jsonDumps(next_state)
        self.response.set_status(201)
        self.response.headers['Content-Location'] = state_key
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(message)

    def saveNextState(self, user, next_state):
        user_id = user.user_id()
        return StateStorage.store(user_id, next_state)

    def getState(self, user, state_key):
        user_id = user.user_id()
        return StateStorage.fetch(user_id, state_key)

    def _preamble(self, state_key):

        # No state_key means the URL didn't include one.
        if not state_key: # Return some sensible homepage.
            self.response.out.write(html)
            return None, None

        user = users.get_current_user()
        assert user # This should be guarded in app.yaml.

        # Retrieve state.
        state = self.getState(user, state_key)
        if not state:
            self._noStateError(state_key, user.user_id())
            return None, None

        return user, state

    def _noStateError(self, state_key, uid):
        self.error(404)
        self.response.out.write(
            '404 <br>\n'
            'No such state: %s <br>\n'
            'User id: %s' %
            (state_key, uid)
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
