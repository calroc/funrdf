import logging, traceback
from google.appengine.ext import webapp
from google.appengine.ext.webapp.xmpp_handlers import CommandHandler
from google.appengine.ext.webapp.util import run_wsgi_app
from models import Fact


XMPP_LOG = logging.getLogger("XMPP")
XMPP_LOG.setLevel(logging.DEBUG)


class XMPPHandler(CommandHandler):

    def message_received(self, message):
        # Guard against random people 'talking' to the app.
        if not message.sender.startswith('forman.simon@gmail.com'):
            XMPP_LOG.warning('received message from %r' % message.sender)
            return
        super(CommandHandler, self).message_received(message)

    def hello_command(self, message):
        reply = 'Bwah! %r' % message.body.lower()
        XMPP_LOG.debug(reply)
        message.reply(reply)

    def know_command(self, message):
        parts = message.body.split()

        if len(parts) != 4:
            reply = 'Bwah! %r' % message.body
            XMPP_LOG.debug(reply)

        else:
            _, subject, predicate, object_ = parts
            reply = 'know: %s => %s => %s' % (subject, predicate, object_)
            XMPP_LOG.debug('attempting to ' + reply)
            try:
                Fact.know(subject, predicate, object_)
            except:
                XMPP_LOG.exception(reply)
                reply += '\n' + traceback.format_exc()

        message.reply(reply)

    def unhandled_command(self, message):
        reply = 'Unknown command: %r' % (message.body,)
        XMPP_LOG.debug(reply)
        message.reply(reply)


application = webapp.WSGIApplication(
    [('/_ah/xmpp/message/chat/', XMPPHandler)],
    debug=True,
    )


def main():
    run_wsgi_app(application)


if __name__ == "__main__":
    main()
